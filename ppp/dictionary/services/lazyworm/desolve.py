import string
import re

from dictionary.models import Word, Translation, Phonetic, Speech


lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
char_to_escape = upper_alphabet + [' ', '.', '-']
kk_chars = lower_alphabet + ["'"]
kk_chars = ["[" + kkc for kkc in kk_chars]


def clean_meaning(x):
    x = re.sub('[/a-zA-Z,. )(&=/}{"]', "", x)
    x = re.sub(u"\u3000", "", x)
    return x


def remove_bracket(x):
    return re.sub("[\（\(\[\<\〈].*?[\〉\>\)\）\]]", "", x)

n_speech = Speech.objects.get(rep="n")
v_speech = Speech.objects.get(rep="v")
vi_speech = Speech.objects.get(rep="vi")
vt_speech = Speech.objects.get(rep="vt")
adj_speech = Speech.objects.get(rep="a")
adv_speech = Speech.objects.get(rep="ad")

with open("dictionary/services/lazyworm/lazyworm.idx", "rb") as idx:
    with open("dictionary/services/lazyworm/lazyworm.dict", "rb") as dictionary:
        word = b''
        scanned = True
        while (byte := idx.read(1)):
            if bytes(byte) == bytes(b'\x00'):
                word_str = word.decode(encoding='UTF-8')
                word = b''
                i1 = bytes(idx.read(4))
                i2 = bytes(idx.read(4))
                word_data_offset = int.from_bytes(i1, byteorder='big')
                word_data_size = int.from_bytes(i2, byteorder='big')
                dictionary.seek(word_data_offset)
                definition = dictionary.read(word_data_size)
                definition_str = definition.decode(encoding='UTF-8')
                if any(to_skip in word_str for to_skip in char_to_escape) or word_str in ['afterski', 'amberfish',
                                                                                          'ankylostomiasis',
                                                                                          'arsenobenzol', 'benzalcohol',
                                                                                          'benzamidoxime',
                                                                                          'benzilidene', 'benzylamine',
                                                                                          'benzylidenei', 'buteo',
                                                                                          'cattlestop', 'cineast',
                                                                                          'dear', 'diazane',
                                                                                          'doppleganger', 'drampers',
                                                                                          'echiuroid', 'foggage', 'fud',
                                                                                          'glycosidation', 'hemale',
                                                                                          'henzylate', 'hottie', 'hoy',
                                                                                          'hydrazinium',
                                                                                          'immaterialise',
                                                                                          'jargonization', 'kayf',
                                                                                          'levodopa', 'lowan',
                                                                                          'masurium', 'metif',
                                                                                          'motortruck', 'naturetin',
                                                                                          'nebuly', 'nett',
                                                                                          'nielsbohrium',
                                                                                          'novarsenobenzene', 'oxazine',
                                                                                          'oxim', 'oxime', 'paty',
                                                                                          'peptonemia', 'phenmethyl',
                                                                                          'pisay', 'pupfish', 'rateen',
                                                                                          'ratteen', 'renderset',
                                                                                          'rockskipper', 'sabertooth',
                                                                                          'scorpionfish', 'semicolon',
                                                                                          'serran', 'serranid',
                                                                                          'sickout', 'signatum',
                                                                                          'stilbamidine', 'stilbazole',
                                                                                          'supersleuth', 'thianthrene',
                                                                                          'tirwit', 'trevally',
                                                                                          'unhoped', 'upsadaisy', 'ux',
                                                                                          'ux', 'vigesimo', 'vingtetun',
                                                                                          'wassat', 'whatchamacallit',
                                                                                          'whatsisface', 'whipray',
                                                                                          'woadwaxen', 'yowman', 'zap',
                                                                                          'zastruga']:
                    continue
                if word_str == "afficionado":
                    scanned = False
                    continue
                if scanned:
                    continue
                # print(word_str)

                # print(definition)
                # print(definition_str)
                translations = []
                speeches = []
                for content in definition_str.split('\n'):
                    if content.startswith('[') or content.startswith('<') or content.startswith(
                            '(') or content.startswith('〈'):
                        if re.search("[\u4e00-\u9FFF]", content):
                            # possible category
                            # print(content)
                            # if content.find(']') != -1:
                            #     right_b = content.find(']')
                            # elif content.find('>') != -1:
                            #     right_b = content.find('>')
                            # elif content.find(')') != -1:
                            #     right_b = content.find(')')
                            #
                            # category = content[1:right_b]
                            # translation = content[right_b+1:len(content)]
                            # print("Cat: " + category)
                            translation = remove_bracket(content)
                            translation = clean_meaning(translation)
                            if translation:
                                translations.append(translation)
                            # print("translation: " + translation)
                            pass
                        else:
                            # kk
                            # print(content)
                            pass
                    elif content.startswith("adj.") or content.startswith("adv.") or content.startswith(
                            "n.") or content.startswith(
                        "v.") or content.startswith("vt.") or content.startswith("vi.") or content.startswith(
                        "pl.") or content.startswith("prep.") or content.startswith("pref.") or content.startswith(
                        "interj.") or content.startswith("conj.") or content.startswith("pron.") or content.startswith(
                        "art.") or content.startswith("aux.") or content.startswith("num.") or content.startswith(
                        "int."):
                        dot = content.find(".")
                        speech = content[0:dot]
                        if speech == "adj":
                            speech = "a"
                        elif speech == "adv":
                            speech = "ad"
                        speeches.append(speech)
                        # print("Speech: " + speech)
                        pass
                    else:
                        translation = remove_bracket(content)
                        translation = clean_meaning(translation)
                        if translation:
                            translations.append(translation)
                        # print(translation)
                        pass
                # for trans in translations:
                #     if all(u'\u4e00' > c or c > u'\u9FFF' for c in trans):
                #         print(word_str)
                #         print(trans)

                translations_str = ', '.join(translations)
                if translations_str:
                    # print("Tranlations: ", translations_str)
                    w = Word.objects.filter(rep__iexact=word_str)
                    if w:
                        continue
                        w = w.first()
                        print("Found " + w.rep)
                    else:
                        w = Word.objects.create(rep=word_str)
                        print("Created " + w.rep)
                    t = Translation.objects.create(word=w, rep=translations_str)
                    for s in speeches:
                        if s == "n":
                            s_obj = n_speech
                        elif s == "v":
                            s_obj = v_speech
                        elif s == "vi":
                            s_obj = vi_speech
                        elif s == "vt":
                            s_obj = vt_speech
                        elif s == "a":
                            s_obj = adj_speech
                        elif s == "ad":
                            s_obj = adv_speech
                        else:
                            s_obj, created = Speech.objects.get_or_create(rep=s)
                        t.speeches.add(s_obj)
                # print('word_str:', word_str, ',word_data_offset:', word_data_offset, ',word_data_size:', word_data_size)
                word = b''
            else:
                word += byte
