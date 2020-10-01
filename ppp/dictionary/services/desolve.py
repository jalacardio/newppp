import string
from dictionary.models import Word, Translation, Phonetic, Speech

lower_alphabet = list(string.ascii_lowercase)

relation_txt = open("dictionary/services/stardict-langdao-ec-big5-2.4.2/relations.txt", "w+")

def replace_dot_word(actual_str):
    translation = actual_str.replace('...', ' ... ')
    return translation.strip()

def replace_dot(idx, actual_str):
    is_in_block = False
    while idx >= 0:
        parenthesis = actual_str[idx]
        if parenthesis == ")":
            break
        elif parenthesis == "(":
            # in ()
            is_in_block = True
            break
        else:
            idx -= 1
    if is_in_block:
        translation = actual_str.replace('...', '某人/事/物', 1)
    else:
        translation = actual_str.replace('...', '(某人/事/物)', 1)
    return translation

with open("dictionary/services//stardict-langdao-ec-big5-2.4.2/langdao-ec-big5.idx", "rb") as idx:
    with open("dictionary/services//stardict-langdao-ec-big5-2.4.2/langdao-ec-big5.dict", "rb") as dictionary:
        word = b''
        while (byte := idx.read(1)):
            if bytes(byte) == bytes(b'\x00'):
                word_str = word.decode(encoding='UTF-8')

                i1 = bytes(idx.read(4))
                i2 = bytes(idx.read(4))
                word_data_offset = int.from_bytes(i1, byteorder='big')
                word_data_size = int.from_bytes(i2, byteorder='big')
                dictionary.seek(word_data_offset)
                definition = dictionary.read(word_data_size)
                definition_str = definition.decode(encoding='UTF-8')
                relatives = []
                dots_idx_word = word_str.find("...")
                if dots_idx_word != -1:
                    word_str = replace_dot_word(word_str)
                w = Word.objects.create(rep=word_str)
                print("WORD:", word_str)
                split_definition_str = definition_str.split("\n")
                for i, sent in enumerate(split_definition_str):
                    sent = sent.strip()
                    if sent.startswith("*"):
                        kk = sent[2:(len(sent) - 1)]
                        Phonetic.objects.create(word=w, kk=kk)
                        # print("KK: {}".format(kk))
                    elif sent.startswith("相關詞組"):
                        sub_sent = split_definition_str[(i + 1):len(split_definition_str)]
                        relatives = [e.strip() for e in sub_sent]
                        break
                    elif sent.startswith("【"):
                        right_bracket = sent.find("】")
                        lexical = sent[0:right_bracket + 1]
                        lexical = lexical[1:len(lexical) - 1]
                        meaning = sent[right_bracket + 1:len(sent)].strip()
                        Translation.objects.create(word=w, category=lexical, rep=meaning)
                        # print("詞型：", lexical, ",譯：", meaning)
                    elif sent.startswith("<<"):
                        meaning = sent[2:len(sent) - 2]
                        Translation.objects.create(word=w, rep=meaning)
                        # print(meaning)
                    elif sent.startswith("a.") or sent.startswith("ad.") or sent.startswith("n.") or sent.startswith(
                            "v.") or sent.startswith("vt.") or sent.startswith("vi.") or sent.startswith(
                        "pl.") or sent.startswith("prep.") or sent.startswith("pref.") or sent.startswith(
                        "interj.") or sent.startswith("conj.") or sent.startswith("pron.") or sent.startswith("art.") or sent.startswith("aux.") or sent.startswith("num."):
                        dot = sent.find(".")
                        speech = sent[0:dot]
                        s, created = Speech.objects.get_or_create(rep=speech)
                        meaning = sent[dot + 1:len(sent)].strip()
                        t = Translation.objects.create(word=w, rep=meaning)
                        t.speeches.add(s)
                        # print("Speech", speech, "meaning", meaning)
                    # When its not only content like "肆虐後平息"
                    elif sent[0] in lower_alphabet:
                        relation_txt.writelines(word_str + "," + sent + "\n")
                        # print(sent)
                    else:
                        dots_idx = sent.find("...")
                        while dots_idx != -1:
                            sent = replace_dot(dots_idx, sent)
                            dots_idx = sent.find("...")
                        Translation.objects.create(word=w, rep=sent)
                        # print(sent)
                if relatives:
                    # print("Relatives:", relatives)
                    relatives = []

                # print(definition_str)
                # print('word_str:', word_str, ',word_data_offset:', word_data_offset, ',word_data_size:', word_data_size)
                word = b''
            else:
                word += byte
relation_txt.close()

