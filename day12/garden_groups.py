# https://adventofcode.com/2024/day/12

input = '''BBBBBBBBGGGGGGGGGDDDDDDDDDDDDDXXXXXXXXXPPPPPPPPPPADDDDDDPPPDDDNNNNNNIXXXDXLLLLLDDNDDUUUGGGGGGGGGGGGGGGFFFSSMSSIIIIIIIIIIIIQGGGGGDDDDDDDDDDDD
BBBBBBGGGGGGGGGGGGGDDDDDDDDDDXXXXXXXXFXPPPPPPPMPPAADDDDPPPPPNNNNNNNNXXXXXXXLLLLLDDDDUDUGGGGGGGGGGGGGGFFFFFSSSSIIIIIIIIIIIQQGGGGGDDDDDDDDDDDD
BBBBBBBGTGGGGGGGGGGDDDDDDDDDXXXXXXXXXXXPPPPPMMMPAAADPPDPPPPPPPENNNNNXXXXXXXXLLLDDDDDDDGGGGGGGGGGGGGGGGGASSSSSSSIIIIIIIIIIQQGGGGGDDDDDDDDDDDD
BBBBGGGGGGGGGGGGGGGDDDDDDDDDDXXXXXXXXXXXQPPMMMMAAAJPPPPPPPPPEEENNNNNXXXXXXWXXXLDDDDUDDDDGGGGGGGGGGGGGGGSSSSSSSSISIIIIIIQIIQGGGGGDDDDDDDDDDDD
BBBGGGGGGGGGGGGGGGDDDDDDDDDDDDXXXXXXXXXQQQPPMFFFAAJPPPPPPPPEENNNNNNXXXXXXXXXXXDDDDDDDDDDGGGGGGGGGGGGGGSSSSSSSSSSSIIIIIQQQQQQQGQGGDDDKDDDDDDD
BBBBGGGGGGGGGGGGGGDDDDDDDDDDXXXXXXXXXXXXWQQQMFFAAAAPPPPPPPPNNNNNNNXXXXXXXXXXXDDDDDDDDSSDSSGGGGGGGGGGGYSSSSSSSSSSSIIIIIIQQQQQQQQGGGHHKDDDDDDD
BBBBGGGGGGGGGGGGGDDDDDDDDDDDDXXXXXXXXYYXWQQQQFFAAAAAKPPPPPPPPNNNNNXXXXXXXXXXXDDDDDDDDSSSSSSSSGSSGGGGGGSSSSSSSSSSSIIIIIIQQQQQQQGGGHHHHMDDDDDD
DDBBGFGGGGGGAAAAGQDDDDDDDDDDDDXXXXXXQYYYQQQQQQQNAAPPPPPPPPPPNNNNNNXXXXXXXXXXXDDTTTTTTTTTTTSSSGSSSSSGGGSSSSSSSSSSIIIIIIQQQQQQQQQGGHHHHHHHDFDF
DBBBAAGGGGLGDDDDDDDDDDDDDDDDDXXXXXXXQYQQQQQQQQQNABPPPPPPPPPPPNNNNNXNXXXXXXXXBDDTTTTTTTTTTTSSSSSSSSSGSSSSSSSSSSSIIIIIIQQQQQQQQQQHGHHHHHFFFFFF
DAAAADDGEEEEEEEEDDDDDDADDDDDDXXXXXXTQQQQQQQQQQNNNBBBPPPPPPPPNNNNNNNNNXXXXXXXXXXTTTTTTTTTTTTTSTTTTWSSSSSSSSSSSSSIIIIQQQQQQQQQQQQHHHHHHHHFFFFF
DAAAADDDEEEEEEEEEEEEEDDTLDDDDEXXXTTTQQQQQQQQQQQQQBBBBJPPPPNNNNNNNNNNXXXXXXXXTTQTTTTTTTTTTTTTTTTTTTWSSSSSSSSSSASQQQQQQQQQQQQQQQHHHHHHHHHFBFFF
DDDDDDDEEJEEEEEEEEEEEEDDLLLDDTDXXXTTTQQQQQQQQQQQBBBBBPPPPXNNNNNNNNNNNXXXXXXXTTQQQQQQQBBTTTTTTTTTTTWDSSSHHHHHHASGZPQQQQQQQQQQQQQQHWHHHHBBBBFF
DDDDDDDDDWWEEEEEEEEEEEDLLLLCCTTTTTTTTTQQQQQQQQQQQBBBBBPPPXNNNNNNNNNNNXXXXXXDQQQQQQQQQBBTTTTTTTTTTTDDDHHHHHHHHAHZZPPQZQQQQQQQQQQQQQDDHHBBBBBB
DDDDDDDDWTWWWWWEEEEEEELLLLCCCTTTTTTTTTTQQQQQQQQQQBBBBBBBPXNNNNNNNNNNXXXXXXXXXDQQQQQQQQQTTTTTTTTTTTDDDMHDHHHHHHHZZZZZZQQQQQQQQQQQQQDHHBBBBBBB
DDDDDDDWWWUWWWWEEEEEEELLLLLCCCCTTTTTTTTTTQQQQQQQBBBBBBBBXXFENNNNNNNNXXXXXXXXCQQQQQQQQQQQEQWTTTTTTTDDDDDDDHHHHHCZZZZZZZQQQQQQQQQQQQDHRBBBBBBB
DDDDDDDWWWWWWWWWNEEEEELLLLTTTTTTTTTTTTTTTQQQQQBBBBBBBBBXXFFFFFFFNNRNXXXXXXXXQQQQQQQQZQQQQQWTTTTTTTDDDDDDDHHHHHHZZZZZZZQQQQQQQQIQLQVMVABBBBBB
DDDDDDWWWWWWWWWWNNEEEEEEELLTTTTTTTTTTTTTTTTTTQBBBBBBBBXXXFFFFFFFFHFKFXXXXXSSSSSQQPPQQQQQWWWTTTTTTTDDDDDDDHHHHHHZZZZZZZZQZZZQQQQLLLVVVVVBBBBB
DDDDDDDWWWWWWWWWWNNNGEZZZTTTTTTTTTTTTTTTTTTTTBBBBBBBBBXXXFFFFFFFFFFFFKXKXXSSSSSSSSPPPPQQWWWWWTTTTDDDDDDDHHHHHHHZZZZZZZZZZZQQQQLLLLLVVVVVBBBB
DDDDDDIWWWWWWWWWWNNNNNNZNSSGXTTTTTTTTTTTTTTTTBBBIIBBBBXXXFFFFFFFFFFFKKKKXJVJSSSSSSSPPPQWWWWWWDDDDDDDDDDDPPHHHHHZZZZZZZZZZZZZZQQXLVVVVVVBBBBB
ZZZZZZIIWWWWWWWWWNNNNNNNNSGGXTTTTTTTTTTTTTTTTTIIIBBBBXXXXFFFFFFFFFFFFKKKXJVJSSSSSSQPPPQQQQWWWDDDDDDDDDDDDDNHHHZZZZZZZZZZZZZZZXXXVVVVVVVVBBBB
ZZZZZIIIIDWWWWWWWNNNNNNNNNNGGJJTTTTTTTTTKTTKKKIIIIIIBXXXFFFFFFFFFFFFKKJJJJJJJSSSSQQQQQQQQQIIIDDDDDDDDDDDDNNNNNZZZZZZZZZZZZZZZXXXVVVVVVVVVBBB
ZZZZZZZIIIIIWWWNNNNNNNNNNNNRGGTTTPPPPPPKKKKKIIIIIIIIXXIXXXFFFFFTTFFFKJJJJJJJSSSSSSQQQQQQQIIIIDDDDDDDDDDDDDNNNNNZZZZZZZZZZZZLLXVVVVVVVVVVBBBB
ZZZZZZZIIIIIWWEEEEEEEEEENNNNGGGTTPPPPPPKKKVKKKIIIIIIIIIIXXFFFFFFJJJJJJJJJJJJJSSSSSQQQQQQQIIIIDDWDDDDDWWDNNNNNNNZZZZZZZZZZZZLLXXXXVVVVVVBBBBB
ZZZZIIIIIIIIIIEEEEEEEEEENNNNGGGVVPPPPPPKKKVVKKIIIIIIIIIIIIFFFFFFJJJJJJJJJJJJJJSSSQQQQQQQQIIIIIIIDDDDDGWNNNNNNNNNZZZZZZZZZZZLXXXXXVVVVVBBBBBB
ZZZZIIIIIIIIIIEEEEEEEEEENNGGGGGGVPPPPPPVVKVVKVIIIIIIIIIIIIITFFFFIIIJJJJJJJJJJPPSSTQQQQQQQIJIIIJJDDDGGGNNNNNNNNNZZZZZZBZZZZZLXXBXXXXVVVVBBBBB
ZZZZIIIIIIIINNEEEEEEEEEENGGGGGGVVPPPPPPVPPPPVVVIIIIIIETIITTTTFFFIIIIJIJJJJJJJPSSTTQQQQQQQZIIJJJJJJJGGANNNNNNNNNNZZZZZBYYYYBBBBBBXXBBBBBBBBBB
ZZZZIIIIIIINNNEEEEEEEEEEGGGGGGVVVPPPPPPPPPPPVVVIIIIIRETITTTTTTFFIIIIIIIJJIJJJJIIIIQQQQQQQZZZZZJJHHGGGANNNNNANNNNZBZZZBBBBBBBBBBBXXBBBBBBBBBB
ZZZIIIIIIIIEENEEEEEEEEEEGGGGGGGVVPPPPPPPPPPPPIIIIIIIIETTTTTTTTFIIIIIIIIIIIJJJJIIIQQQQQQZZZZZZHHHHHHFAAAAPANAANNNABZZZBBBBBBBBBBBBXXXBBBBBBBB
ZZZIIIIIIEEEEEEEEEEEEEEENNGGGGHHVPPPPPPPPPPPBIIIIIIIIEEETTTTTTFIIIIIIIIIIIJIIIIIQQQQQQQZZZUZHHHHHHLHHAAAAAAAAANNABBBBBBBBBBBBBBBBXXXBBBBBBBB
DZZIIIIIIEEEEEEEEEEEEEEERRDGGGVVVPPPPPPPPPPPPPPPPPPIEEEEETTTTFFFIIIIIIIIIIJIIIIIQQQQQQJJJZZZHHHHHHHHHHAAAAAAAHNNNBBBBBBBBBBBBBBXXXXXXBBBBBBB
DIIIIIIIIEEEEEEEEEEEEEEERDDGGVVVVPPPPPPPPPPPPPPPPPPEEETTETTTFFFFIIIIIIIIIIIIIIIIIEQQQQIIIOYYHHHHHHHHHAAAAAAAAANNNBBMBBBBBBBBBBBBXXXXXBBDBBBB
DIIIIIIDEEEEEEEEEEEEEEEERDDGVVVVVVVPPPPPPPPPPPPPPPPKEETTTTTTFFFFFFIIIIMMIIIIIIIIIIIQQQIIIYYYHHHHHHHHHAAAAAAAAAABNBBBBBBBBBBBBBBBXXXXXXDDDBBB
DIIIIDDDEEEEEEEEEEERRRRRDDDDDDDVDDDPPPPPPPPPPPPPPPPRRRTTTTTTTFFFFFMMMMMMMMIIIIIIIIIIIIIIIIYYHHHHHHHHHAAAAAAAABBBBBBBBWBBBBBBBBBBXXXXXXUUDBBB
DDIDDDDDEEEEEEEEEEERRRRRJDDDDDDDDHVPPPPPPPPPPPPPPPPRMTTBTTTFFFFFFFFFFMMMMMMIIIIIIIIIIIIINNYYHHHHHHHHAAAAAAAAAABBWBABWWBBBBBBBGGBUUXSUUUUUBBB
DDDDDSSSSEEEEEEEEEERJJRJJJDDDDDDHHMPPPPPPPPPPPPPPPPRMTTTTTTFFFFFFFFFMMMMMMMMMMIIIIIIIINNNNYYNHHHHHHHHHAAAAAAQWWWWWAWWWBBBBBBBGGBUUXSUUUUUUUB
DDDDDSSSSEEEEEEEEEERJJJJJDDDDDHHHHHPPPPPPPPPPPPPRRRRRRTTTTTFFFFFFFFFFMMMMMMMIIIIIIIIIINNNNNNNNHHHHHHHHAAAAAAWWWWWWWWWWWBBBBBBBBUUUXUUUUUUUUU
DDDDSSSSSSSSSSSSRRRRRAAJJJDGDDHHHHHHHPPPPPPPPPPPRRRRRRTTTTTFFFFFFFFFFFMMMMIIIIIIIIIIINNNNNHHHHHHHHHHZHAAAAAAWWWWWWWWWWWWWWSSBBUUUUUUUUUUUUUU
DDDDDSSSSSSSSSSSRRRHHHHJJDDGDHHHHHHHHPPPPPPPPPPPRRRRRRTTTTTFFFFFFFFFFFMMNIIIIIIIIIIIINNNNNNNHNHHHHHHZZZAIIIWWWWWWWWWWWWWWWSBBBAUUUUUUUUUUUUU
DDDDDDDSSSSSRSSSSHHHHHHJDDDGDDHHHHHHHPPPPPPPPPPPRRRRURHTTTFFFFFFFFFFFFFNNIIIIIIIIISINNNNNNNNNNNHHHHHAZZZIIIWWWWWWWWWWWWWWWSSBAAUUUUUUUUUUUUU
DYDDDDDSSSSSRSRRHHHHHHHHHDGGTTTTTTTTTTPPPPPPPPPPRRRRURHTTTTTUFFFFFFFFFNNNIIIIIIIIISSSNNNNNNNNNNHHHHHZZZZWWWWWWWWWWGWWXXWWXXSXXAUUTUUUUUUUUUU
YYYDDDDSSSSRRRRRRHHHHHHHDDGGTTTTTTTTTTPPPPPPPPPPRRDDTTHTXTUUUFFFFFFNNFYNYIIITIISSSSSSSNQQQQQQAAAAAAHZZZZWWWWWWWWWGGWWXXXXXXXXXXTTTUTTUUUUUUU
YYYYDEEEESRRRRRRRHHHHHHHHGGGTTTTTTTTTTPPPPPPPPPPRDDTTTTTTTUUFFFFFFFNNYYYYYYTTTSSSSSSSSNQQQQQQAAAAAAZZZZZZWWWWWWGGGGWWWWXXXXXOOOXTTTTJJJUUUUU
YYYYYETYESEEEQQQQQQQQQQHGGGGTTTTTTTTTTPPPPPPPPPPRRRTTTTTTTUUFFFFFFNNNNYYYYYTTTTSSSSSSNNSSSQQQAAAAAAZZZZZZWIIIGGGGGGWKWXXXXXXOOOXXXXXJJJUUUUU
YYYYYTTYEEEEEQQQQQQQQQQGGGGGTTTTTTTTTTPPPPPPPPPPRTRTTTTTTTUUUTFFNNNNYYYYYYYTYTSSSSSSSSSSSNSSSAAAAAAZZZZZZWIIGGGGGGGWWXXXXXXXOOOXXXJJJJJJJUUU
YYYYYYYYYEEEEQQQQQQQQQQQGGGGTTTTTTTTTTPPPPPPPPPPTTTTTTTTTTTTTTTTTTNNYYYYYYYYYTSSSSSSSSSSSSSSSAAAAAAGGGZZZIIIGGGGGGGSWWWXXXXXOOOXXUJJJJJJJJUU
YYYYYYYYEEEEEEEEHHHQQQQQGGGGTTTTTTTTTTTTTTTTPPPPTTTTTTTTTTTTTTTTTTYYYYYYYYYYYTSSSSSSSSSSSSSSSAAAAAAGGGRZZZIGGGGGGGGXXVXXXXXXOOOXXUJJJJJJJJJU
YYYYYYYYYYEEEEEEEHHQQQQQGGGGTTTTTTTTTTTTTTTTPPPPWTTTTTTTTTTTTTTTTTYYYYYYYYYYYTTSSSSSSSSSSSSSSAAAAAAGRRRZZGGGGGGGGGGXXXXXXXXXOOOXXUUJUJJJJJJU
YYYYYYYYKYEEEEEEEEEQQQQQGGGGTTTTTTTTTTTTTTTTPPPPTTTTTTTTTTSTTTTTTTYYYYYYYYYYSSSSSSSSSSSSSSSSSAAAAAARRRRZZGYGGGGGGGGGXXXXXXXXOOOMMUUUUJJJJJJU
YYYYYYYYEEEEEEEEEEEQQQQQGGGGTTTTTTTTTTTTTTTTWWTTTTTTTTTPTTSTYTTTTTYYYYYYYYSSSSSSSSSSSSSSSSSSSSSSSMRRRRRRYYYGGGGGGGGAAAAXXXXXXXXMMJJJJJJJJJJG
YYYYYYYYYEEEEEEEEEEQQQQQGGGGGGGGHWTTTTTTTTTTTTTTTTTTTPPPPPSSTTTTTTYYYYYYYYYSSSSSSSSSSSSSSSSSSSSSSSRRRRRRYYGGGGGGGGGPAAAAXXMMMMMMMGJJJJJJJJGG
YYYYYYYYYYEEEEEEEEEQQQRRGGGGGGGGWWTTTTTTTTTTTTTTTTTTPPPPPPSPSSTTTTYYYYYYYYYSSSSSSSSSSSSSSSSSSSSSSRRRRRRGGGGGGGGGGGAAAAAAAAMMMMMMGGGGGJJJJJGG
YYYYYYYYYYEEEEEEEEEQQQRRGGGGGWZWWWTTTTTTTTTTTTTTTTTTPPPPPPPPPPTTTTTYYJJYYYYYYYSSSUSSSSSSSSSSSSSSSRRRRRRGGRGGGGGGGFAAAAAAAAMMMMMMGGGGGGGJGGGG
YYYYYYYYYYEEEEEEEEEQQQRRRGGZZWWWWWTTTTTTTTTTWWWTTTTTTTPPPPPPPPXTTTGJYJJYJJJJYYYSSUSSSUSSSSSSSSSSSRRRRRRRRRRRRLLLLAAAAAAAMMMMMMMMMGGGGGGGGGGG
YYYYYYYYYMEEEEEEEEEQQQRRRGGHZZZHWWWWWWWWWWWWJJQTTTTTTTTPPPPPPPPGTTGJJJJJJJJJYYYYYUUUUUSSSSSSSSSSSRRRRRRRRRRLLLLLLAAAAAAAFMMMMMMMMMGGGGGGGGGG
JYYYYYYNNMMMMEEEEEEQQQRHGGGHHZHHWWWWWWWWWWWWWJQTTTTQQTTPPPPPPPPGGGGJJJJYJJJJYYYYYUUUYYYUSSSSSSSSSRRRRRRRRRRLLLLLLAAAAAAAMMMMMMMMMMMGGGGGGGGG
JJYYYMYNNMMMMEEEEEMQQQHHHIHHHHHHHHWWWWWWWWWWQQQTTQQQQTTPPPPPPPPGGGGJJJJJJJJJYJYYYUUUYYYUUSSSSSXXSRRRRRRRRRRLLLLLLALLAAAMMMMMMMMMUMMGGGGGKGKG
JJYKYMMKKKMQQQQQQQQQQQHHHHHHHHHHHHHWWWWWWWWWQQQQQQQQQQPPPPPPPPPGJGJJJJJJJJJJJJYLYUUUYYYUUSUUSSSSWWSRRRRRRLLLLLLLLLLLMTMMMMMMMMMMMMMMMGGGKKKG
JJJKKMMKKKKQQQQQQQQQQQHHHHHHHHHHHHHHHWWWWWWWQQQQQQQQQQPPPPPPPPPJJJJJJJJJJJJJJJLLUUUUYYYUUUUUSSSSSWSSRRRLLLLQLLLLLLLLMMMMMMMMMMMMMMMGMGGKKKKK
VVKKKKMKKKKQQQQQQQQQQQHHHHHHHHHHHHHHHWWWWWWSQQQQQQQQQQPPPPPPPPPJJJJJJJJYYYYYYNNLUUUUYYYUUUUUSSSSSSSSSQQQQLQQQLLLLLLLLMMMOOMMMMMMXMGGGGGKKKMK
VVKKKKKKKKKQQQQQQQQQHHHHHHHHHHHHHHHHHHHHWWWSSQQQQQQQQQPPPPPPPHPPHHJJJJJYYYYYYYYYYYYYYYYYYUUUSSSSSSSSTQQQQLQQLLLLLLLEMMMMOOMMMGMGGGGTTGGKKKKK
VVKKKKKKKKKQQQQQQQQQHHHHHHHHHHHHHHHHHHHSSWSSSQQQQQQQQQPPPPPPPHHHHHJGGJJYYYYYYYYYYYYYYYYYYVVVVSSSSSSSQRQQQQQQQLLLLLEEEOOOOMMMMGGGGTTTTKKKKKKK
VVKKKKKKKKKQQQQQQQQQHHHHHHHHHHHHHHHKKKKKSSSSSQQQQQQQPPPPPPPPHHHHYYYYYYYYYYYYYYYYYYYYYYYYYVVVVSSSSQQQQQQQQQQQQLLLLNEEEEEOMMMGMGGGGGTTTKKKKKKK
VKKKKKKKKKKQQQQQQQQQHUUUUHHHHHHHHUHKKKKKSSSSSSSQQQQQQSSPPPPPHHHHYYYYYYYYYYYYYYYYYYYYYYYYYVVVYVSSSSQQQQQQQQQQQLLNNNNEEEEEEMGGGGGGGGGTTTKKKKKK
VKKKKKKKKKKQQQQQQQQQUUUUUHHHHHZHHUHKKKKKSSSSSSSQSQQSSSSSPQPHHHHGYYYYYYYYYYYYYLLLLLLYYYYYYVVVVVSSSSQQQQQQQQQQQQLNNNNEJJGGGGGGGGGGGGGTTTTTKKKK
VKKKKKKKKKKQQQQQQQQQUUUUUUUUHHKKKKKKKKKKSSSSSSSSSSQSSSSSPPPPGGGGYYYYYYYYYYLLLLLLLLLYYYYYYVVVSSSSSSQQQQQQQQQLLLLNNNNNJJJJGGGGGGGGGGGTTTTTKKKE
VKKKKKKKKKKSSMMBMMUUUUUUCUUUHKKKKKKKKKKKKSSSSSSSSSSSSSSSSSPSSGGGYYYYYYYYYYLLLLLLIILYYYYVVVVVVSSSSSSSQQQQQQQQRRLNJNJJJJJGGGGGGGGGGGGTTTTTKEEE
VVKKKKKKKKKIIBBBBMEUUUUUCUUHHKKKKKKKWKKKSSSSSSSSLLLSLSSSSSPGGGGGGGGGGGQQQQLLLLLLLLLLLVVVVVVVVSVSSSSSSSQQLQRRRRRJJJJJJJJGGKGGGGGGGGUTTTTTKEEE
VVKKKKKKKKKIIBBBEMEEUUUCCCCCCCKHKKKKWWWWUUSUSSSLLLLLLSSSSSSGZGGGGGGGGGQQQQQQULLLLVVVVVVVVVVVVVVSSSSSSSQQQQRRRJRJJJJJJJDLGGGGGGEGGGUUTTTTTEWE
VVKKKKJKIKIIIBBEEEEEUUUUUUCCCCCCKKKKWWWUUUUULSSLLLLLSSSSSSSZZZGGGGGGGGQQQQQQLLLLLLVVVVVVVVVVVVSSSFSSSSSSRRRRRJJJJJJJJJDLLLLLDEEEDUUUUUUUUWWE
VVVKKKJKIKIIEEEEEEEEEUUUUUCCCCCCCKKKWKWWUUUULSSLLLLSSSSSSSSSSZGGGGGSGQQQQQQLLLLXXVVVVVVVVVVVVVAAFFSFFSSSRRRRRRJJJJJJJJDLLLDDDEDDDDUUUUWUUWWW
VVVKKIKKIIIIIEEEEEEEEUUUUUCCCCCCCCPKKKWUUUUULLLLLLSSSSSSSSSSSZGGGGSSSQQQQQQQLLLLRRVVVVVVVVVVAVAAFFFFFFFSRBBBRRJJJJJDDDDDDDDDDDDDDDUUUWWWWWWW
VVVKIIIIIIIIIEEEEEEEEUUUXCCCCCCCCCCKKKUUUUUUULXLLLQQQSQQQSSSQGGGGSSQQQQQQQQQHLRRRVVVSVVVVVVVAAAAFFFFFFBSNBOBOBBJJJBBDDDDDDDDDDDDDUUUUWWWWWWW
IIIIIIIIIIIIIIIEEEEEEUUXXEXCCCCCCCCYKUUUUUUUUXXLLLQQQQQQQQQQQGGGSSSSQQQQYYQQQRRRRRVVVVVVVVVVAAAAFBBFFFBBBBBBBBBBBBBBDDDDDDDDDDDDDUUUUWUWWWWW
IIIIIIIIIIIIIIIEEEEEEUXXXXXCCCCCCCCYUUUYUYUUUXXXRVQQQQQQQQQQQGQQQSSSSQQQRQQQRRRRREVVPVVVVVVVVAAYJYFFFYBBBBBBBBBBBBBBSDDDDDDDDDDDDUUUUUUWWWWW
IIIIIIIPIIIIEEEEEEEEEXXXXXXZZZCCCCCYYYUYYYYUUXRRRRQQQQQQQQQQQQQSSSSSSSSRRRRRRRRREEVEEYVVVVVVAAAYYYYYYYBBBBBBBBBBBBBBBDDDDDDDDDDDDUUUUUUWWWWJ
IIIIIIIIIICCEEWEEEBXXXXXXXXZZZZCCCZYYYYYYYYYYRRRRRRRQQQQQQQQQQQQSSSSSSSRRRRRRRRRREEEEYYAVVVVAAAAAYYYYYYBBBBBBBBBBBBBDDDDDDDDDDDDDUUUUUUWWWWJ
IIIIIIIIIIIIIEWWEEEEXXXXXXXZZZZZZZZZZZYYYYYYYRRRRRRRQQQQQQQQQQQSSSYSSSRRRRRRRRRREEEJEEEAAAAAAAAAAYYYYYBBBBBBBBBBBBBBDDDDDDDDDDDDUUUUUUUUWWJJ
IIIIIIIIJIIIIWWWCCEEMMXXXXXZZZZZZZZZZYYYYYYYYRRRRRRRRQQQQQQQQQQQSSYSSSRRRRRRRRRRRREJJEAAAJJJJAAAYYYYYYYBBBBBBBBBBVVVEEDDDDDDDDDDUUUUUUUUWJJJ
IIICIIIIIIIIIIIWWCEEMMXXXXXXZZZZZZZZZHHHYYUUYRRRRRRRRRQQQQQQQQQYYYYYYRRRRRRRRRRRRRJJJJJJAJJJAAAAAAYYYYYYYBBBBBBBBBVVVVDDHHDDDDDDUUUUUUUUUUJJ
IIIIIIIIIIIIIIIWWCCCMMMXXXXZZZXZZZFZVVHHYYUUURRRRRRRRRRQQQQQQQQQYYYYYRRRRRRRRRRRRRRJJJJJJJJJAAAAAYYYYYYYYPBIBBBBBBDVVHHHHHDDDDDUUUUUUUUUUUJJ
IIIIIIIIIIIIIIIWCCCMMMXXXXXXXXXXZZHHHHHHYUUUURRRRRRRRRRRQQQQQQSYYYYYYRJRRRRRRRRRRRJJJJJJJJJXXAAAYYYYYYYPPPBBBBBBBVVVVVHHHHHDDDDUUHHHUUUUUJJJ
IIIIIIIIWIIIIYYYYYCYXXXXXXXXXXXXZZXXHHHHUZUURRRRRRRRRRRRQQIQQYYYYYYYYYJJRRRRRRRRRJJJJJJJXJJXAAAPPPPPPPYPPPPPBBBBVVVVVVVVHHHHHDHHHHHUUUUUGGGG
IIIIIIIIIIIIIYYYYYYYXYXXXXXXXXXXXXXXXXHHUUUUURRRRRRRRRRLQQIYQYYYYYYYYJJJRRRRRRRRRRRJJJJXXXXXAAPPPPPPPPPPPPPPPBBBVVVVVVVVHHHHHHHHHHHUGGUGGGGG
IIIIIIIIIIIIIYYYYYYYYYXXXXXNXXXXXXXXXJHHUUUUUUUUURRZRRRRQQYYYYYYYYYYYJJYYRBBBAARBRRJXXXXXXXXXXXXPPPPPPPPPPPPPPPPVVVVVVVHHHHHHHHHHHHULGGGGGGG
IIIIIIIIIIIIIYYYYYYYYYYYYXXNXXXXXXXXXXHHHHUKUUUUURRZZRZRKQYYYYYYYYYYYYYYBBBABABRBRRBXBBXXXXXXXXXPPPPPLLPPLPLLPPPPVVVVVVHHHHHHHHHHHHUGGGGGGGG
IIIIIIIIIIIIIYYYYYYYYYFFFNNNNNXXXXXXXXHHHHUUUUUUUZZZZZZYYYYYYYYYYYYYYYYYBBAAAABBBEBBBBXXXXXXXXXXXXPLLLLLLLLLLPPPPPPHVVHHHHHHHHHHHHHUUGGGGGGG
IIIIIIIIIYYYYYYYYYYYYYFFFNNNCNXXXXXHHXHHHHHUUUUUUZZZZZZZZYYYYYYYYYYYYYYYBBAAAAPBBEBBBBXXXXXXXXXXXXPPLLLLLLLLLPPPPPPHHHHHHHHHHHHHHXUUGGGGGGGG
IIIIIIIIIYYYYYYYYYYYYFFFFNNNNJJJJXXHHHHHHHHHZZUUZZZZZZZZZZYGYYYYYYYYYYYYAAAAABBEBBVVVVVVVVXXXXXXXXXXLLLLLLLLLLPPPPPPHHHHHHHHHHHHHHOOGGGGGGGG
IIIIIIIIIWYYYYYYYYYYYFFNNNNNNJJJJXXXSHHJJJXJJZZZZZZZZOOZZZYGYYYYYYYYYAYAAAAAABBBBBVVVVVVVVXXXXXXXXXXLLLLLLLLLLPPPPPPPPPPPPPPPHHHHHOOGGGGGGGG
GGGWWWWWWWYYYYYYYYYYYYFFFNNNNJJJJSSASSHJJJJJJJJZZZOOOOOZZZYYYYWYYYYYYAAAAAAAAABBBBVVVVVVVVXXXXXXXXXXLLLLLLLLPPPPPPPPPPPPPPPPPHHHHOOOOGGGGGGG
GGGGWWWWWWYYYYYYYYYYYMXFFFNNNJJJSSSSSWJJJJJJJJZZOOOOONNOOOOOBYWWWWWAAAAAAAAAAAABBBVVVVVVVVXXXXXXXXLLLLLLLLLLLPPPPPPPPPPPPPPPPOHHHOOOOOGGGGGG
GGGWWWWWWWYWNYFYYYYYYMXFFNNNNNSSSSSJJJJJJJJJJJOOOOOOOOOOOOOZOYWWWWAAAAAAAAAAAAABBBVVVVVVVVXXXXXXXXLLLLLLLLLLLLLPPPPXPXXPPPPPPPHHHHHHHOGGGGGG
GGGGGWWWWWWWWWFFFYFXFFXXXXXXTNZSSSSJJJJJJJJJNGGGOOOOOOOOOOOOOWWWWWAFFAAAAAAAAAAABBVVVVVVVVXMXXXXXXTTTLLLLLLLLLLPPXPXXXXPPPPPPPHHHHHHHGGGGGGG
GGGMGGWWWWWWWWFFFFFFFFXXXXXXXSSJSSSJJJJJJJJGGGGGOOOOOOOOOOOOOOWWWAFFFAAAAAAAAAAIIHVVVVVVVVVVVVVXXXTTTLLLLLLLLLLLLXXXXXXTXPPPPPPPHHHHHZGGGGGG
GGGGGGWWWWWKKKFFFFFFMMMMMMMMMSSSSSSJJJJJJJJJGCGGGGOGGOOOOOOOOBIWWAAFFAAAAAAAAAAAHHVVVVVVVVVVVVVGXXTTTTELLLLLLGLGLXXXXXXXXPPPPPPPHHHHHZZZGGGG
GGGGRRWWWWWWWFFFFFFFMMMMMMMMMSSSSJJJJJJJJJJJPJGGGGGGGGOOOOOBBBIIAAAANNNNNNNNNNAAHHVVVVVVVVVVVVVGXXTTTTLLLLLLLGLGGXXXXXXXXPPPPPPPHHHHHZZZGGGG
GGRRRRRRRRRRRRFFFFFFMMMMMMMMMSSSSSJJJJJJJJJJPJGGGGGGGGGGGOOBBIIIAAAANNNNNNNNNNAEHXXXHHHOVVVVVVVGGGGTTOLLLLLLLGGGGXXXXXXXXPPPPPPPHHHHHZZZGGGG
RRRRRRRRRRRMMMMMMMMMMMMMMMMMMSSSSSSJJJJJJJJJJJJGGGGGGEGEOOBBBBIIIAAANNNNNNNNNNEEXXXXXHHHVVVVVVVGGGTTTTIILLLLLGGGXXXXXXXXXPPPPPPPHHHHHZZZGGGZ
RVRRRRRRRRRMMMMMMMMMMMMMMMMMMSSSSJJJJJJJJJJJJJJGGGEGGEEEEEBBBBIIINNNNNNNNNNNNNXXXXXXXUHHVVVVVVVWGGGTTTIILLFLGGGGXXXXXXXXXPPPHHHHHHHHHZZZGGGZ
VVVVRRRRKKKMMMMMMMMMMMMMMMMMMZZSSJJJJJJJJJJWJJGGGGEGGEUUUUBBBBBBINNNNNNNNNNNNNXXXXXXXXHHVVVVVVVWGGGGGYIILLLGGAGGGXXXXXXXXPPPHHHHHHHHHDZZZZZZ
VVVRRKKKKKKMMMMMMMMMMMMMMMMMMZZZZJJJJJJJQJXJJXXEEGEEEEUUUUEEIIIIINNNNNNNNNNNNNXXXXXXXXXHVVVVVVVVVGGGGYIILGGGGAGGGGGXXXXPPPHHHHHHHHHHHDDDZZZZ
VVVRKKKKKKKMMMMMMMMMMMMMFFPZZZZZJJJJJJJJJJXXXXEEEEEEEEUUUUEEIIIIINNNNNNNNNNNNNXXXXXXXXXHVVVVVVVVVGGGGYIAAAGGAAGGGGGGXXXPPPHHHHHHHHHHHDDDDDZZ
VVVRKKKKKKKMMMMMMMMMMMMMFPPZZZZZZZZZJJYYYJXXAEEEEEEEEEUUUUEMEIINNNNNNNNNNNNNNNXXXXXXXXWWWWWVVVVVVWWGGYYAAAAAAAAAAGGGGGGPPPHHHHHHHHHHHDDYDDZZ
VVVVVVKKKKWMMMMMMMMMMMMMPPPPPSZZZZZZZJYYYYAAAEEEEEEEEEUUUUEEEIINNNNNNNNNNNNNNNXXXXXXXWWWWVVVVVVVVWGGGGGAAAAAAAAAAGGGGGGGPPHHHHHHHHHHHDDDDDDZ
VVVVVVJJVKKKWWWIIIHHHHHHHPPPPSSSZZZZZZPPYYAAAAAEUUUUUUUUUUEIIIINNNNNNNNNNNNNNNXXXXXXXJJJWVVVVVVVVWGGGGGGAAAAAAAAAAAGGGGPPPHHHHHHHHHDDDDDDXDZ
PVVSVVVVVKWWWWWIHHHHHHHHHHPPPSSSSZZPPPPPAYAAAAWAUUUUUUUUUUYYIIINNNNNNNNNNIXXXXXXXXXXXJJJJVVVVVVVVWWWWGGAAAAAAAAAAAAAGRRPRFHHHHHHHHHDDDDDDDDD
PVSSVVVVVVWWWWIIHHHHHHHHHLLPSSSSSZZPPPPPAAAAAAAAUUUUUUUUUEYYIIINNNNNNNNNNIXXXXXXXXXXJJJJJVVVVVVVVWWWWGGGAAAAAAAAAAARRRRRRRHHHHHHHHHDDDDDDDDQ
VVVVVVVVHVWWWIIIIIHHHHLHLLLLLLSSZZPPPPPPAAUUUUUUUUUUUUUUUEYIIIIIIIIINNNNNXXXXXXXXXXXJJJJJVVVVVVVVWWWGGGGGGAAAAAROOORRRRRRRZZZZHHHHDDDDDDDDDD
VVVVVVVIIIIIIIIIIHHHIKLLLLNLLLSSZZPPPPPPAAUUUUUUUUUUUUUUEEYYIIIIIIIINNNNNGGGXXXXXXXXJJJJJVVVVVVVVWWWWWGAAAAAAAARRORRRRRRRRZZZZHHHHZDDDDDDDDJ
QQVVVVVVVBIIIIIIIIIIIKLLLLLLLLLLLPPPPPPPAAUUUUUUUUUUUUUUEYYIIIIIIIIGNNNNNGXXXXXXXXXXXXXJZXWWWWWWWWWWWGGGAAAAAAARRRRRRRRRRRZZZZHHHHDDDDDDDDJJ
QVVVVVVVIIIIIIIIIIIIIIILLLLLLLLLLLPPPPPPPAUUUUUUUUUEEEXEEEYIIIIIIIIKNNNNNGXXXXXXXXXXXXXXXXWWWWWWWWWWWQGGGAAAAAAARRRRRRRRRZZZZZHHHHDDDDDDDDDJ
QVVVVVVVIIIIIIIIIIIIIIILLLLLLLLLLLPPPSPPPAUUUUUUUUUEEEEEEEYQAIIRIIIKGGGGGGXXXXXXXXXXXXXXXXXWWWWWQWWQQQGGGGGAAAAARRRRRRRRRRZZZZZZZZZDDDDDDKDJ
VVVVVVVVVIIIIIIIIIIIIIIQLLLLLLLLLLLLLLPJJJUUUUUUUUUJJJQQEEYQQQRRRRGGGGGGGGXXXXXXXXXXXXXXXXXWXWWWQWQQQQGGGGGGGAARRRRRRRRRRRRZZZZZZZZDDDDDDDHH
VVVVVVIIIIIIIIIIIIIIIQQQLQLLLLLLLLLLJJJJJJUUUUUUUUUJQQQQQQQYYQRRRRRRGGGGGGXXXXXXXXXXXXXXXXXXXXXXQQQQQQGGGGGGIHRRRRRRRRRRRRRRZYYZZZZZDYHHHHHH
VVVVVVIUUUIIIIIIIIIIIQQQQQLLLLLLLLLLLJJJJJUUUUUUUUUJQQQQQQQQYQQRRJRGGGGGXXXXXXXXXXXXXXXXXXXXXXXGGEQQQQGGGIIIIIJRRRRRRRRRRRRRYYYYZYYZYYYHHHHH
VVVVVVVUUVIIIIIIIIQQQQQQQQLLLLLVLLLLLJJJJJUUUUUUUUUJJQQQQQQQQQRRJXXXXXXXXXXXXXXXXXXXXZZZZXXXXXXGEEQQEGGGGIIIIIIPPRRRRRRRRRRRYYYYYYYYQYYHHHHH
VVVVVVVVVVVZIIIIIQQQQQQQQQLLLVLVJJLJJJJJJJUUUUUUUUUJJQQQQQQQQQRJJXXXXXXXXXXXXXXXXXXXXZZZGXHHEEEEEEEQEGGGIIIIIIPPPRORRRRRRRRRKYYYYYYYYYYYHHHH
QVVVVVVVVVZIIIIIIQQQQQQQQQQQLVLVVJJJJJJJJJJJJJJJJQQQQQQQQQQQQQQJJXXXXXXXXXXXXXXXXXXXXZZZZVHHHEEEEEEEEGGGIIIIIIIIIOORURRRKRRKKYYYYYYYYYYYHHHH
QQVVVVVVVPIIFFIIIIQQQQQQQQQQQVVVVVVVVJJJJJJJJJJJJQQQQQQQQQQQQQQJJJJJJJJKXXXXXXXXXXZZZLLLZVHHEEEEEEEEEGGGIIIIIIIIIIOOINNRKKRKKYYYYYYYVVYHHHHH
QQQQVVVVVVIIIIIIQQQQQQQQQQQQVVVVVVVJJJJJJJJJJJJJJQQQQQXXQQQQQQGOJJJJJJJMXXXXXXXXXXZLLLLLVVVHEEEEEEEEEEEEEIIIIIIIOOOOIINRKKKKKYYYYYYYYVYHHHHH
QQQVVVQQQQIIMIIQQQQQQQQQQQKQQVVVVVVJJJJJJJJJJJJJJQQQQQXXXXQQQQOOJJJJJJWMXXXXXXXXXXZCLLLLVVVEEEEEEEEEEEEEEEIIIIIIIIIIIIRRKKKKKYYZYYYYYYHHHHHH
QQQQQQQQQQQMMLQQQQQHHQQQQKKQQQVVNNKKJKKJJJJJJJJJJIQQQQQXXXXOZQOOJJJJJJWWXXXXXXXXXXZLLLLVVVEEEEEEEEEEEEEEEEIIIIIIIIIIIIIIIIIKKYYZZCYYYYYHHHHH
QQQQQQQQQQQQMLQQQQQHHHQQQQKQQQQQQNKKKKKKQQQIEJJJJIQQQIIIIIXOQQOOJJJJJWWWXXXXXXXXXXZLLLAAAVEEEEEEEEEEEEEEVVXIVVVIVIIIIIIIIIIIIYZZZCYYYYYHHHHH
QQQQQQQQQQQQLLLLLQQQQHHHHHKKYQYFYNKKKKKKQIIIJJIJIIIIIIIIIIOOOOOOOJJWWWWZXXXXXXXXXXVVVLAAAAAEEEEEEEEEEEEEVVVVVVVVVIIIIIIIIIIIZZZZCCHHHHHHHHHH
QQQQQQQQQLLLLLLLQQQQQHHHHKKKYYYYYYBKKKKKIIIIIJIIIIIIIIIBOOOOOOOOOOAAWWWWWZZOVVVVVVVVVVVAAAAAAAEEEEEEEEEEVVVVVVVVVIIIIIIIIIIIIIZCCCCHHHHHHHHH
QQQQQQQQLLLLLLLQQQQQHHHHHKKKKCYYYYGGGKKKIIIIIIIIIIIKKIIBBOOOOOOOOAAAWWWWWZZOOOOVOOVVAAVAAAAAAAEEEEEEEEEVVVVVVVVVIIIIIIIIIIIIIZZCCCCCHHHHHHHH
QQQQQQQLLLLLLLLLLQQQQHHHKKKKKYYYYYGGKKIIIIIIIIIIIIIKKHRRRREOOOOOOAAAAAWWWWWOOOOVOOOAAAAAAAAAAAEEEEEEEEVVVVVVVKKIIIIIIIIIIIIZIZZCCCCCKKHHHHHH
QQQQQQQLLLLLLLLLLLLLLHHHHHKKKKYKKKKGKKIIIIIIIIIIIIIKKRRRRRROOOOOOAAAAWWWCOSOOOOOOOOAAAAAAAAAAEEEEEEEEEVVVVVVVKDDKFIIIIIIIIZZZZZGCCCCKKHHKHHH
QQQQQQLLLLLLLLLLLLLWBHHHHZZKKKKKKKKKKKKIIIIIIIIIIIIKKRRRRRRROOOOAAAAQCCCCOOOOOOOOOOAAAAAAAAAAEEEEEPPEVVVVVVVVVDDKFFFIIIIIIZZZZZGGGCCKKKKKKHH
QQQQQQLLLLLLLLLLLLLWBWHHHHHKKKKKKKKKKKKIIIIIIIIIIIIKKRRRRRRRRLRAAAAAQQQQOOOOOOOOOOOAAAAAAAAAAAAEEPPPPVVVVVVVVADDFFFFIFIIZZZZZZGGGCCKKKKKKKKK
QQQQQQLLLLLLLLLLLLLWWWHHKKKKKKKKKKKKKKKIIIIIIGIIIIIIIIRBRSRRRLRRAQQQQQQQOOOOOOOOOOOAAAAAAAAAAAAAEEPPPPVVVVVVVADDDFFFFFIIIZZZZGGGGCCKKKKKKKKK
QNNNQQLLLLLLLLLLLLLWWWWWKKKKKKKKKKKKKKKIIIIIIGIIGIGIIIRRRRRRRRRRRRRQQQQQQQOOOOOOQOAAAAAAAAAAAGGGEEPPPPVQVQVVQDDDDFFFIIIIZZZZZZZGGGCCKKKKKKKK
QQNNQHUOOLLLLLLWWWWWWWWWKKKKKKKKKKKKKKKKGGGGGGGGGKGIIRRRRRRRRRRRRRRRQQQQQQQQOOOQQAAAAAAAAAAAAAAGEEPPPPQQQQQQQDDDDDDDIIIIIIPZZZZZGMMCCCKKKKKK
NNNNNUUUOLLLLLLWWWWWWWWKKKKKKKKKKKKKKKKKGGGGGGGGGKGIRRRRRRRRRRRRRXXQQQQQQQQQQQQQQQQAAAAAAAAAAAAGEDPPPPPPQQQQQDDDDDDDIIIIIIZZZZZZGZMMCCKKKKKK
NNNXNUUUUULLXLLLWWWWWWKKKKKTKKKKKKKKKKKKGGGGGGGGGGGRRRRRRRRRRRRRRXXQQQQQQQQQQQQQQQQAAAAAAAAAAGGGGPPPPPPQQEQQQDDDDDDDIIIIIZZZZZZZZZMMCCCKKKKK
NNNXUUUUUXLXWWWWWWWWWWTTTTTTKKKKKKKKMGHKGGGGGGGGGGRRRRRRRRRRRRRRRRQQQQQQQUQQQQQQQQQQAAAIIAAAGGGGGGGGPPEEEEDQDDDDDDDDDIIIZZZZZZZZZMMCCCMPKKKK
NNXXUUUUUXXXXWWWWWWWWWWWTTTTKKKKKKKKMGGGGGGGGGGGGGGRRRRRRRRRRRMMRMMMQQUUQUUQQQQQQQQQQAAQQGAGGGGGGGGGPEEEEEDDDDDDDDDDDIIIZZZZZZZZZMMMMCMPMMKK
XXXXXXXXXXXXXXXWWWWWWWWTTTTTTKKKKKTTGGGGGGGGGGGGGGGGRRRRRRRRRMMMMMMMMMUUUUUUUQQQQQQQQAAQQGGGGGGGGGGGPEEEEDDDDDDDDDDDKMMIZZZZZZZZZZMMMMMMMMKK
XXXXXXXXXXXXXXWWWWWWWWWTTTTTTTTTKTTTGTTGGGGGGGGGGGGGGRRZRRRRRRRMMMMMMMUUUQQQQQQQQQQQQQAQQQGGGGGGGGGGEEEEEEDDDDDDDDDDKMIIZJZZZZZZZZMMZZTMKKKK
XXXXXLXXXXXXXXXWWWWWWCTTTTTTTTTTTTTTTTGGGGGGGGGGGGGGGZZZZRVVRRRRMMMMMMUUUUQQQQQQQQQQQQQQGGGGGGGGGGGGEEEEEEYDDDDDDDDDDMMMZJJZZZZZZZZZZZTTKKKK'''

example_input = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

test_input = '''AAABBBCD
DBBBCCCA'''



def load_garden(input):
    garden = []
    lines = input.split('\n')
    for line in lines:
        row = []
        for s in line:
            row.append(s)
        
        garden.append(row)
    
    return garden


def find_regions(garden):
    regions = dict()

    for y in range(len(garden)):
        for x in range (len(garden[0])):
            plant = garden[y][x]
            if plant not in regions.keys():
                regions[plant] = []
            
            plot_regions = []
            for region in regions[plant]:
                for plot in region:
                    if are_adjacent(plot, (x, y)):
                        plot_regions.append(region)
                        break

            if len(plot_regions) == 0:
                new_region = [(x, y)]
                regions[plant].append(new_region)
            elif len(plot_regions) == 1:
                plot_regions[0].append((x, y))
            else:
                primary_region = plot_regions[0]
                for r in range(1, len(plot_regions)):
                    secondary_region = plot_regions[r]
                    for plot in secondary_region:
                        primary_region.append(plot)

                    regions[plant].remove(secondary_region)

                primary_region.append((x, y))

    return regions


def are_adjacent(left, right):
    xdiff = right[0] - left[0]
    if xdiff < -1 or xdiff > 1:
        return False
    
    ydiff = right[1] - left[1]
    if ydiff < -1 or ydiff > 1:
        return False
    
    return xdiff == 0 or ydiff == 0


def region_cost(region):
    return perimeter(region) * len(region)


def perimeter(region):
    p = 0
    for plot in region:
        p += count_non_neighbour_sides(plot, region)

    return p


def count_non_neighbour_sides(plot, region):
    count = 0
    for side in range(4):
        if not has_neighbour(plot, region, side):
            count += 1

    return count


def has_neighbour(plot, region, side):
    for other in region:
        if is_neighbour(plot, other, side):
            return True
        
    return False


def is_neighbour(plot, other, side):
    xoffset = 0
    if side == 1:
        xoffset = 1
    elif side == 3:
        xoffset = -1

    xtarget = plot[0] + xoffset
    if other[0] != xtarget:
        return False
    
    yoffset = 0
    if side == 0:
        yoffset = -1
    elif side == 2:
        yoffset = 1

    ytarget = plot[1] + yoffset

    return other[1] == ytarget



garden = load_garden(input)

regions = find_regions(garden)

cost = 0
for plant in regions:
    for region in regions[plant]:
        rc = region_cost(region)
        cost += rc

print(cost)

# The answer for part 1 is 1930 for the example_input
