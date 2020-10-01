from dictionary.models import Word, Meaning, Speech

import string

lower_alphabet = ['m']
# lower_alphabet = list(string.ascii_lowercase)
for alpha in lower_alphabet:
    relation_txt = open("dictionary/services/websters/{}.txt".format(alpha), "r")

    while True:
        line = relation_txt.readline()
        if not line:
            break
        line = line.rstrip()
        if line == "":
            continue
        first_space = line.find(" ", 1)
        left_bracket = line.find("(", 1)
        right_bracket = line.find(")", 1)
        word = line[0:first_space]
        tense = line[left_bracket+1:right_bracket]
        meaning = line[right_bracket+2:len(line)]
        if tense in ["v. t. & i.",  "v. i. & t.", "v.t & i.", "v. t.", "v. i.", "v. i. & i.", "v. t.& i.", "v. t. & v. i."]:
            tense = "v"
        elif tense in ["P. pr. & vb. n.", "p. pr. & v. n.", "p. pr. & vb. n.", "p. pr & vb. n.", "p. pr.& vb. n.", "p. pr. & vvb. n.", "p. pr. & vb. n", "p pr. & vb. n.", "p. pr. & vb n.", "p. pr. & vb/ n.", "p. pr. & vb, n."]:
            tense = "ppr,v,n"
        elif tense in ["p. p. & vb. n."]:
            tense = "pp,v,n"
        elif tense in ["p. pr. & a."]:
            tense = "ppr,a"
        elif tense in ["p. pr. & vb."]:
            tense = "ppr,v"
        elif tense in ["p. pr. & vb. a."]:
            tense = "ppr,v,a"
        elif tense in ["v. i. & auxiliary."]:
            tense = "v,auxiliary"
        elif tense in ["imp. & p. p.", "imp. &. p. p.", "Archaic imp. & p. p.", "imp.& p. p.", "imp. & pp."]:
            tense = "imp,pp"
        elif tense == "prep. & adv." or tense == "adv. & prep.":
            tense = "prep,adv"
        elif tense in ["prep., adv. & a."]:
            tense = "prep,adv,a"
        elif tense in ["prep. & conj.", "conj. & prep."]:
            tense = "prep,conj"
        elif tense in ["prep., adv., & conj.", "adv., prep., & conj."]:
            tense = "prep,adv,conj"
        elif tense in ["prep., adv., conj. & n."]:
            tense = "prep,adv,conj,n"
        elif tense in ["adv. & a.", "a. & adv.", "a & adv."]:
            tense = "adv,a"
        elif tense in ["adv. & n.", "n. & adv.", "adv., & n."]:
            tense = "adv,n"
        elif tense in ["a., adv., & n."]:
            tense = "a,adv,n"
        elif tense in ["a., n., & adv."]:
            tense = "a,v,adv"
        elif tense == "n., a., & v.":
            tense = "n,a,v"
        elif tense in ["a. & v.", "a. & v. t.", "v. & a."]:
            tense = "a,v"
        elif tense in ["a. & n.", "n. & a.", "a & n."]:
            tense == "a,n"
        elif tense in ["v. & n.", "n. & v.", "v.& n.", "n.& v."]:
            tense = "v,n"
        elif tense in ["n. & i."]:
            tense = "n"
        elif tense == "adv. & conj.":
            tense = "adv,conj"
        elif tense in ["adj. & conj."]:
            tense = "adj,conj"
        elif tense in ["imp. & obs. p. p.", "obs. imp. & p. p."]:
            tense = "imp,obs,pp"
        elif tense == "prep., adv. & conj.":
            tense = "prep,adv.conj"
        elif tense in ["p. p. & a.", "p. p & a.", "a. & p. p.", "P. p. & a.", "a & p. p.", "p. p. & a", "p. p. & p. a."]:
            tense = "pp,a"
        elif tense in ["n. & v. t.", "v. t. & n.", "v. i. & n.", "n. & v. i.", "n. / v. t. & i.", "n & v.", "n. & v"]:
            tense = "n,v"
        elif tense in ["sing. & pl."]:
            tense = "sing,pl"
        elif tense in ["n. & pl."]:
            tense = "n,pl"
        elif tense in ["n. sing. & pl.", "n. sing. & pl", "n.sing. & pl.", "n.sing & pl.", "n. sing & pl.", "n., sing. & pl."]:
            tense = "n,sing,pl"
        elif tense in ["pron. & a.", "a. & pron.", "a. & a. pron."]:
            tense = "pron,a"
        elif tense in ["pron. & conj."]:
            tense = "pron,conj"
        elif tense in ["pron., a., & adv."]:
            tense = "pron,a,adv"
        elif tense in ["pron., a., conj., & adv."]:
            tense = "pron,a,conj,adv"
        elif tense in ["dat. & obj."]:
            tense = "dat,obj"
        elif tense in ["n. & interj.", "interj. & n."]:
            tense = "n,interj"
        elif tense in ["p. p. &"]:
            tense = "pp"
        elif tense in ["p. pr. & vb. e."]:
            tense = "ppr,v"
        elif tense in ["p. a. & vb. n."]:
            tense = "pp,a,v,n"
        elif tense in ["p. pr. a. & vb. n."]:
            tense = "ppr,a,v,n"
        elif tense in ["p. pr. & pr. & vb. n.", "p. pr. &, vb. n.", "p, pr. & vb. n.", "p. pr. &vb. n.", "p. pr. &. vb. n."]:
            tense = "ppr,v,n"
        elif tense in ["imp. &, p. p.", "imp. & p. p.,", "imp. &. p.", "imp. & p. p", "imp. & p. p", "imp. &p. p."]:
            tense = "imp,pp"
        elif tense in ["imp. & p. pr."]:
            tense = "imp,ppr"
        elif tense in ["imp., p. p., & a."]:
            tense = "imp,pp,a"
        elif tense in ["imp. & p. p. & vb. n."]:
            tense = "imp,pp,v,n"
        elif tense in ["imp. & p. pr. & vb. n."]:
            tense = "imp,ppr,v,n"
        elif tense in ["imp. sing. & pl."]:
            tense = "imp,sing,pl"
        elif tense in ["imp. sing. & pl."]:
            tense = "imp,sing,pl"
        elif tense in ["pres. & imp."]:
            tense = "pres,imp"
        elif tense in ["interj. & adv."]:
            tense = "interj,adv"
        elif tense in ["interj., adv., & n."]:
            tense = "interj,adv,n"
        elif tense in ["inf. & plural pres."]:
            tense = "inf,pl"
        else:
            tense = tense.replace(".", "")
            # if tense.find("&") != -1:
            #     # if tense == "v. t. &":
            #     #     print(word)
            #     #     print(tense)
            #     #     print(meaning)
            #     print(tense)
                # pass
        print(word)
        print(meaning)
        print("----------")
        if word == "Middler":
            quit()
        w = Word.objects.filter(rep__iexact=word.lower())
        if w:
            print("Found " + word)
            m = Meaning.objects.create(rep=meaning, word=w, source="Webster's Unabridged Dictionary")
        for speech in tense.split(","):
            s, created = Speech.objects.get_or_create(rep=speech)
            m.speeches.add(s)
        # # print(tense)
        # print(meaning)

    relation_txt.close()
