# https://adventofcode.com/2024/day/19

data = '''rwrwr, ruu, bwwubu, ugrubg, wg, wbg, ugr, bgr, uruug, ruubw, rwr, rwbbb, rrrgb, ruru, wggru, ruw, bgu, wgg, ggbbbb, rr, guwwbw, gru, bwurb, bbwburg, ubb, wuuuu, urb, brwr, uwr, rruww, ubgwgwr, ugb, urbgwug, bub, grrb, wugbr, ggwu, bug, ruuw, ugwu, brurgb, rug, uwg, rrw, rgrggwu, rgbrr, brgr, rwrbu, ggw, wrbrb, bgwb, urgr, brgub, rwbbwub, rwgbur, wggr, wurww, wbbgwg, rw, urbu, grgbwu, ru, uuuguu, bwuggbrr, buw, ubgw, gburrb, urwbb, ububggg, bwbr, bgwug, grr, wggu, rrgu, wwuu, ggu, rggbuu, grwwru, rrbu, bwggrb, ggr, brgu, gbgr, bbubwugg, brrr, uwggru, rrb, rwwwbbu, urrr, guug, u, gwrrugw, wrwgr, guwg, rwu, wuww, wurrg, bugu, wrr, wwrr, bwrrw, guu, ubugb, rguw, uurbb, wuwwuw, uwbbgbwg, uuwruub, bggww, bugbrubu, brwrwbb, gbur, wrgbru, bbu, bgubwgu, uw, gbg, wbwwb, rrruwgw, rgw, bbg, ggwg, wug, bgugr, rwb, bggb, gwww, wwww, bwrwb, rwguwu, rrwrbb, br, wbr, bguu, gurrb, wuw, gurg, ggg, brbrrgr, gruu, rbgb, uwgrw, wwwuu, gbburrru, wbwwww, wgw, gbwb, ugww, gbr, uugrug, gw, rrwu, urg, brr, rb, uwb, wwuuu, bbrwb, gwu, wugrw, ugu, wruwrw, uwuwuuu, bbrru, rgg, urub, gbw, rwgurbwg, rrg, wuwu, uuw, bwur, uurur, wbu, gwguwgr, ggub, rrr, wubb, wbbg, grb, rbwgrr, wbbrguw, ubww, uuwg, ugwrb, grgbgrgg, bgwr, bbuugu, wbb, rurbrrb, wgwgbbr, rgurru, brgwwg, buu, wgu, bur, wwwww, ubbguu, rbrbrbb, rggg, urw, uur, brb, gbuwu, bgrugu, grwgwwb, gbrgrr, uwbbr, brbgrb, bwwwbuub, rwrb, gu, rgrr, bgwubuw, bwwurg, bg, g, rgr, grugbr, rgb, bwb, gbugb, wwr, uruwr, gr, wbgrwww, wwrurb, rugb, rwwwww, uwub, uwrru, wgb, ubr, grg, ggwrr, gwg, rww, wbggw, wurg, bgrwrrw, urru, wuu, wuwgu, ggbgb, ubbgg, wwrrr, rbg, uurg, rgurwugb, wrwg, ubw, gwgg, rbu, bbr, wwu, bwwu, rgwbrbgu, ugrg, guw, rub, ur, rggb, wgr, bu, ggb, wbbug, grw, bwr, uwwwww, wwrwb, brrur, bwbrbur, gwgu, gwuwwru, bgb, bwg, uww, wbubwg, wgrwuw, ugw, uuurrbrw, gww, gbguuw, bbuuwu, rrrr, gwugggu, bwrguu, wgbu, uwrwuww, wuwg, uwwr, gug, bgrw, gur, bwuu, uug, rwbuguu, wwgrr, grgbrw, ub, urrwburr, bgww, rwgu, bwuwwb, gbb, rbru, gwrg, bggu, wu, ggrbu, wubu, bwwg, rbrwb, ugug, rgbrrgbu, rgrruww, wurrw, rgug, ruwrgrgw, wgwgu, guggg, uwggb, uubbru, grurr, uru, wburg, brwwbb, rgwrug, brbub, bwbw, ugrug, wrg, rgrwrugr, urwrr, wuuwr, wwb, bwu, rbw, rwbwru, gwb, rg, bgbur, wwrgugr, rwg, ubu, wgwuu, wub, rwug, bgg, bgw, brw, burrbwgu, ubwuw, r, bruuu, w, rgu, bww, bbb, uubrbbw, rbrr, wb, wwbgwrrw, wrgbwu, gwrrr, wrgubu, wuggb, rgburu, bruug, ugggwur, grbu, wguuw, wr, uuu, wubgwg, bbbuug, wgbrrbg, wwbbgw, wgugbrw, uu, buwwugwu, bgrwwgu, urr, gbubuww, wur, gub, ubbb, urwugwrg, rrgb, brwgb, rwrr, gb, wru, gggu, rbgg, ww, rwrgur, bubb, wrw, ubg, ugwb, rwuurrb, ugg, gubrub, ubwr, uub, rrur, rgwb, gubwu, gbwrbgb, ug, gg, wbbburb, wwubg, bwbgb, gbbwr, ubuw, rgbgbb, ggwgbbb, urbrgu, ubbuwr, ggwr, urug, rru, brg, gbu, gwr, wrggug, rgwwr, bbw, bugwgr, uubg, wbru, uwu, rbwu, bgbrrurw, wrgug, bwbbbu, rbr, www, bbww, rgbbgu, wrb, rubb, gwrbr, uwbwu, uuwr

gugrrrugwbugrrwbbbbggrwbuurgbbgurururuburrbwgugruwubwrggwr
gbgbbrugurggbuuwgwrrbwbwrurrgugwrrburrbgwbugbwgguuurbgwg
bgbwbggburguguubrbwbrugggbuwbbgggbbuggugurur
bbwwbbuburuwrgrgwbrggwbggrrwggwrwuwgrgggbrbrrwuwrrwruburbg
bubgubgrwbbgbuwgwburbwubgbugggbbrbburrbwbwgru
bugbuuguwwruuwgrwwurgbgruruugbbguuguuuwrbrwwrrwggbrggu
uubwgrrrwggwwgwbbwuwgwguurggurrrugbggguwbggbggbuuwg
uwgbwwgwwgwrwwbrruubuugrgrrwbwburgbguuugwrwwgrbbubwwgrbb
ugwbrrurgrurggurbbubuuurwrbugrbbwrrgruururbubggwrwgbu
uwubwrbrrubrrrrwwbwggbrbrwguugubbwbwwurbuwwubrrgb
rurwgwbgburgrbgrbbugrbwbgrrbgguuubrbgggbrgbwurrbb
wguuwwuwwuurwwrgbwuwggrbgwuggwbugwgwgubrggburrgu
bwbwrggbwbbrgwgrbuuwwgwrrwugwugbgbrbbgrubbbgubgrbb
rurbuwwuwwbgrgbwrurburubggbuwbrwruububwurubgwbgrggwbuug
bgbuwrugwuruwrggwguwgrugwwrruwrgrgwuuwrbb
guuugrrgwgggwgbguwwuwwrgwgbbrrrwgurwrggwrrguwubrwgbgbwurg
rggwgggrwgrggwbwwrrbuwwwbrbbgurugwgruuurrwgw
rubuggubrgbbwbuwwrbgggrrbwurrrgbwrgrbgbrwbgbgwb
rwwbruurgbwrguwgbrrrwgubggurgwugubbuuurbuurrgrgbgrgg
bubgbwrbgbgrwggguurgbugbburrrugguguubruwbuwbbg
wbubwwrbuburbgrbwgwbbbwrrbgrgwrgbrurgbrbwggrbbg
bgrbuuwwrwgugwrbrwwurugrubbrwwuwugbuugbggburwuuw
uuuwbgwugruwwwwgggbbggrrwubwgubrwbwwrbwwgwgbruwgrwbuuruw
grburuggrwwbwbgwubrbwburwwggugurgbruuugbubbggwuwbu
ruuuubggguwwggrgwbgubbuwuwwgrbrbrggrwrbwgwrgbugwgbguuurbrbb
rbwrwwwuuruuwgrugurbbbgggrbbwwguwrbrguurgwurbubgrb
bgguurbguwwurrubbuwugwgwrbburuugrrrbbuwrwwgrbur
gwgbwuguwruubwrbwubgggggwrgwbwrrugwbwwbrubrrrrgwwuuggrbgu
rurrggggwwwggburugbwgrwwbbguwgrgwwwwrbgbwrbub
ruububwrugwubgwuuuggwugrgbgrrgrrguuwguwubruugbugbrrgwr
brbguwbgbrrrubbbwwggurbbbuwrbwruurubuggwgrbwgg
gbubgbgrbubbrrurwgurbwgwuwwgurbggwrrrwwggwrwwgrbuuggrbb
urbbwgrggggrrgbrbbuwubruwgrwuwguwgbwbwggbggrwrwu
ggwgugrbubbwrguwbrguwruuwwwbuwugugburrrrrrguwuugrubwrwgrg
bugbuugrubwrbbugggugwubbbwwggrbuwuwbwwurwbbrururbubbw
bgbgwrbwgbuwgwuguburwgugbrgbrrgggrgwwububuw
grgugrbrubrurubrrrggbwrgwbruugwggrbuwbbrgb
wgburwgugrgugbggrgwbuwbwggwuurugurrbbwwwuurgbuurgrruwuwb
wwururubgwugbbbrwgwbrurwgrugbrbrbbwrwggrgrwubbwuuwuwbg
rwuurbwwrrbgbuuwrrbuwbguwrwbuugrwuwbuubgwbugugwbbb
gugubgwbgrubwrrbgguruguruwwbrgwwuwubrgbguwwbbruwwbbwbwuu
uwwbbuwgbbuwwuggbuwgbgrbuwbuuuruurwwgwbbggburggr
wwbrrwwrwubrbwrgggwrbwbbrrurbbrgrrurwguwwbwurr
gugwgrwrwgwrbwrwbgrruwwwuwrurwgrbrgbrgbruwgwrbugrbg
ubrubwwbbrbgwwgwuwwgbbrwbubggbrguuuugurgrwwuwurrgu
bgbubwrgwgbbwuggbrruwuwrguuguwuwrwggwgrurbwugrbb
urgrwggwwuuwrugggubbgubwbruwgrbwbbuwurgrgruwuwbuuuruubuwrb
urbrwbgbubgbrrgrgwwurwbgbwrrgrwgggwbggrwurbrwbwwugbbwu
rwruwrguubbubuggubwgwguubwwwrwguuwwggwrbrurbuu
ruuwrwwrrrrubggggwugggugubbwbwugwuwwbwgrgr
rwubrrgwrbrwgrwwrwuggbbubgggwubwrurrrwgruwrugwwrgwgrbrruw
buuwwgrwuwguuugggrwuwwubbrbgbgbwrggwuwbgwgubbrwug
bubruwubrubwgggwggruugwbrubwrubbwwuurwbrgwwrbguwgwguwgwgrw
buuggwuugggrrggrgbbwbbgbwrwbbguuubwrgbrbbwwwgrwuggrggguwbb
guwrwgrgbbruwugguburuuwbrbrbwwurbwrbrruurubwubuurbu
gbrgrgbrwwguwwrwrbugrgurrwubrgrrubwbgwwburrwbgbrrub
uuguuwuggbgugbubbggrguwruwwgrbbububurrgwwggrruuubrwbwurb
rwbwrbrwwuuubbbbbbbwrubrggwubbbubgrurbbrggwgrgwuwug
buwgwgrguwbrbgrbgrbrgrgrwgwbruwgwrbuubbwbwuubrrgbwbuubggb
uuubuurwuuubwgruwgubrrugugbguwbugugggugrrbrwbugruggwrwgwbu
rwwgbrbuubrrbwgbubwwrwbuurwbwrrrgbwgbbrbbbwr
wbugbrubugggrwbbrwbubbgrbgwggbwrbbgubrbb
rrrrgrgrwrugrwruwgrwwrbgugrwwrrgugrbbbbgbuugrbrbb
wbgbgurgbbuwgrubuuurubbgruurugubgbrurugrggugubwgbwgrw
rgbrrbuwubbbrguwrgurwwubgrgwuguubwurrugwguburgrbgw
wgbguuwwuruuruugwurbgbbgrgwgbwrwuuwwbugurbb
wbwwwrruuguruuwgwwrrguuwugwrwrrwwwuuwwwuwbggrwgbr
gwbgwbrwwbbubrrgugwbruwugugbbgbwrgrrrgwbrbguuugrubw
wwuguwwwrwgwgrurwgbbugugurbwwrwbgrgbbwuwrubggbbgggwgrug
wbbrbruubgrrgrubwgbrwbrbwuwrbubrrubugrgbrwwwwbrgrgwubru
bbugurbrbrrbrgrgggurwugwrggruwuggrubrbwwgbbrbb
guggguwwgrrbuugwwbbbrgbwwwugbwguuruguwggbrwgrgrbbrr
rwuggruwwwgggwbgbbbrbwwubggwbuguwgwubggwrguruww
gwbrubbugrwbgurrrgggrubrgruuugrubbbgrgrrwrwuggwgbrggbwbr
wwwgbbwwbrbrwwgubrgrwrrbbgwuggbrbubbubbbbruugbgurgwgu
bbgwrrgwuwurwrbrrubuwwbwrgwubbuwrgggrwrrwgwuurubugur
rrgwugbggrgrrubbbgubwuwbbgwgwubrwuubwrwgbrrrwbbugbrgrbubrr
brwbwbuugrruuuwrwwgwwurbuwwgwggugubbbugrwgrbrwruwwuwrbgbuu
ububbgrgbbbubrwgrrbruururwwbgbgbwrugwbgrurubuwbrugrrrrbu
brgwuruggrbgggruguwubrbbwbrrgbugbrgggrubwwrrurugrwwggr
gwwbrbwbbggugrwubrubguruuwrurwgwgbwuuggggbrbwgrrbrbrgb
bwugrrubwrburrwbgrwgurbwgbwgbwbburgwwwwbrrbbbwwug
wwbwgrwggbuwuuguburugugggurgrrgrgwwrgugruwwbbbr
rubuugggbrwwbbrrrbrwrwbgubrggubruuuwgguwbbwrwwgwrrr
rwbbwbbwrgbrrggubwrrwurgbgggbuwrbrgurgrubggwbwbrrgr
uwwrrbubgrguwwwgurwwurwbwwgbgwwguwugbbbubbwrwrrwgurubwb
grwrrwruruwbubuuubbuugurrwwwuurbgrrrurbb
uwgbbbuurggwbwwwgbbgwgrrugwruwwrugrwubgrwwrbgwbbgbgrrbb
brwgrugbrgwggruuwbrwwbgwggubrrubrgrwrugrwgwbwr
buwugwwggwbgwbgbwgbugrubgbugugubrbggrbgugwbwgruwwugub
gbugruwwuurrugbggbgggwgwurrwbwurbrwbbggrrbbggrgbrgubbwwwbr
bruuguuubbrrwgubrgrbrbgwuugugwubbrwbwgrbwwrurrbg
wbgwbwurububrbugbgwgbggbgubbrwrubwwuwbuuggggrugrgururgbbu
ggbbubuuuuuuwguwbrbuwwgwuggrubbgbbrggrurbw
bububwgbuwugrurgbubugwwrwbgwrbwuuguwugwugugwubg
wburbububwrurbuwbwrbbwrwbubugwgwbgugwbuwwgwbuu
ugbbwuburbrwrrgwwgurrrbgbuwubbgrrubrwgbbbbgubggbbrruwr
rbbwwuwgbrwbugburubguuurgwbwbwbwggurbguubugruu
uwguwwbggrbbrgwwrubwrrwwubwbwbugburbruguggwwguwurwgwwgw
wrbubbbwrwbwwurwugbrrrubbbbbgggrguwwrrrgbgubbwgug
wbuwuggbwggwwuurwwwubbbbrgbwbrguwurgggbubgrwwbu
grrgrurbbgrwugwggbrgwwwwggrburrububrrrbwgrbrgrrwb
bwwuwwwbuuwrgugwruwwwububggwbgrgwwwuwgbgub
rrrgwwurrwuubwgrrbwuwgrugubwruubrwbbrgwwbgrgrrgbwbuuwwbwwu
gbrbgbrurggubrrggwrwwgubgrwwbrrrugbuuwubbuuruwgrbuurubb
wbgwguwwgbwbbgwgrgbwrbbwbrwwurbgwrrruwuggwbugu
grrbgrrruwwubrwugbwuuurwwwwwgwbgbwrguubrrwurur
wuuwurgururbgbrguwrwrururrurwggwgwwwbwwruwurwuuugwgrggb
rbuuwbbrbwwrgbbbbgbgggwwwuwbwuwwwggwrurwrbb
wbwrrgggwgrrrggrgbwgggrgbbbrrggwbgbwuwruwrugugguwrgwrrrb
bgbugrwbburuwgwrgbbgwbrbbuggbwwurrbgwgggbwgugbwgrwrwgwwu
bbubwuggrbbuwbugwwwgrubrbgrruurrugbrrrgubruwubugbrwr
gbbgbrwugwrggbbbrwbrwwrwbruruwbrbuuugbbuur
wwuggwbbwgbbrgwrbggbggwbgwwgwbgbbrrbrbgrwbrugbgbuwbw
gbbrwubbrbgrgwwgwbruugggwbgugwgugggugrbwwbrrwbubwwgbgwb
bgruwbbugwurbuubrgrugwrurwwruguwbwuuubruwrrrgubrgrgg
ugrbrwguubwgrbrwuruurwurwrrggwrwuwrbgbggbuggwwrbwbubg
uubuuwrurgbuwugugurgwubwwbrbuugwrgbubwbrbrgbggwggggggbwrw
wgrubbrbwbgbwguuuwrbwrbwwgbbbrwgrwwbgrwubgbguwbubbgru
rbuguuwrubbguwrwbuwwugwuggbrurggggwbrwgrwguubguubwrbb
wwbggwgwrbgbwgbgrrbrggggbggubgwrwrbwwbugbgrrbw
ubrwrrbrrrgugbubggugruwgurrrbburuwurggwurwrwubb
rwubgurgwuuuwwwrbugbuwwwwwwrbuuwrrbwgrwbbggbgbwugur
gbwgbrgbwbwwbrruuwwguwwrwrbggwbuuuwuurggrgrugwbgrwgggu
gruguuwbwrbgbwbwuwbguuguubruurguggbrbbrggwwwwrb
uwurrbbugurgrbugguubuugggwuuuruwbgburbwwbugbgubg
gubgruwwrwwbwbbwrrugugrbrwguwwrgwuuuuuwrgubgrbbbgu
bwgurgurburbwbgguurgurbbuwugububuggrbgwbrbgubbgrwwuggw
rbrwgwrrrbwbrwuwbbggwwuwuggrgwrgbrbbrurwbwwgg
rrbwubbbruguuugwbbwugwurgbuuwuugrrwrgruugwrrwruggrbgrb
uwguubwrwrbgurbrubguwggwwggwrgwugguwrrrrgruwwbwwwbguwww
rbbbrwgbbbwuwbbgbwgbgbrrbgrurggwwbguwgwrgubrbb
uwwubuwrgggwbbgurrgugwugruwuuwrwgbrguwrwwbuwrwbbrgbw
uwugrbwwbrbgugggwbwububgbbwuuburrrrgwggubur
grwugggbuubgwrbrwrbbrubrbbuuubuwuwgururruugrwggrwugubuw
bubrgrruwbgwwwuwurbwbwwbbwbrrrggwwrwbbbwwgbru
ggwbbrguubgrbggrwwwbwruguuurbbgwuugwuwuwwwb
uugrwburwruuubwbgbbrrbgggubuwgwubggrbuubgrrbwwurw
gwbburgbgrrguuurguubgurgburbbrwuwwwurgbwbbgwurg
grwwwwwgbbrrguubrwbuuwggggwgugrbwwwrwruggubrwgrwub
rgburggruruubrbbgggbrruuubgwgwururrurrbrbubburuwgbg
bggrbbgwbwuggrrurbrbgrrurubwrbbuuuruububggwwgur
wrwwgbruurbwwgruwbbggwgubwuwruwrwbubwgwuwwb
buwgwbrrwrrrwrrgwwgugwwwbgubgrrgrgguubrbuuubbrwwuuu
rrbgrrwwgururburrrbbuguwwuwwgrrrwwwubrruwrr
wwrwwwwwwgwguwrrgbgurbwbwgbwwburugguwwrbgur
brubbrggrrwbwbbuuubrgrgbwwggwguwuuwbrgguguugrwg
uwwggrrggbbburrrrurbbrrbugwgurbbgwrwwbbubwwuuuwggggbgbwbuu
brbbburgbrbrggwwrgbrbguurwrrwggbwgwwrbbuwrggbwgugrggb
rugbrbgugruuwuwwrbburbbugrwugwwbrwbbbrugwrgwuuu
urrbgurgbwrubbwuguugbbwwubbwrgrruubbgbwurbrbb
bgwgrguruubrwgwrbggbwguwrrbwurgggbgrgwwguwb
bwburubggugubwggwwrurgwwubrurrwbbrubbwrruwbuuwguu
wurwrgggbwgwubruwwbrguurrrrubuwgbrruuubrbb
uurwugwbbgrrgwuruguwugrbwbbwrrrwgwwbwwbrugrwrg
ugwggwgugbwrbwrwgggbgrbrwwubgbbwubwuugwbugbwwbrgrgwrwrbb
wuuurgubuwuurbrbwurbubguwrwgruurrbrbbbguruwgbbwgrgb
ggbrwuwbgrwgbuwbuggubrbgrwwrgwwwwurwurwbug
rbbubuwuwubbbrwubrrwgrubbwwguwuwubwwugbgruwrgb
rbgwurbwgbbbwugbbwwbgwbwwbbrrgruwwubguubgwg
brwbgbbgbwwuburwubwbubgrwuuwbrgubrbbuwwbrrwbuu
guwuwrrurruwrrwuurbrrrgwugrwguruubuwbwrrggrgub
urgrggrwgwrrburrbwgrgguwgwbbwruwbrrubrbuuuguwrr
bwburgubbuubwbbggwrgbrbgwurrwgwurguurbgbggug
gubwwwuwbrggwrwgrrwwuwuuwrgrwrrrwwurrburugubww
wruguwgwbbuwrwuwbbubbbgggbwggrbwurrgrrrbuugrgguwg
buugbwuwuuugrbuurbgrbubugrugugburgbrbbrubuu
rurrgrwrgwwrbrbuwbbuuuubwubwgwrrgrrrbguuuubbrggburugubr
ugurwwwbuwwbbrggubwrwgwgugrguuggurrbbrgubrwru
wrurrrgwrugurgurwrrgbwuwwbwbburubggrggwrwwrur
uwbgwwuwbgggrrrgbgwugrrrurwgurwbugbbrbwuwu
rwwubwgwrwuuguuugbruwuwwrgwuruwrbbuwbrwuwuubrbbbrbrr
bbuwggrwrwbrgbwubwubugggrbruwwuguurgwrrbgugbguruuubuw
rgwugugbwrwbbwgrbrguubugbgguwwgrrbbrbrwgggubbgurbwggg
wurrbubwgbubgrbbbrrbgwuurgbwbwwgrrburbgbgwuruwbbggrb
wwruuuuwuurbwgwrwuwgbbggbuwggguggurugwggubbgbgbrbwww
guuwbrurubrrwbrwuwrbrurubwbubuubgbwubbwwguruw
urububrbwbgbgwwbbrruwgbggurbggruugurrgbwbbgwrwuwuwurbb
rwbbggbrgwwuggubgwurwgrburbrwwrugggurwwwurww
ugwbbbbgubbgbrbruwwwbururgwbbbbbbububgggbwgugbwrrrgr
wgrrbbwburwwwwrwuuurguwggrbbbugwrbgbgwwrwruwu
wrurbbbbguwgbwgurwrwugrubbrgruguwgwbwgbwrwg
ruurgbuuwbwubgruuguubbrbbwuurbrgwgbgbgrwguggggrbg
rrwrwgbwggwrgwwwwwrrbrubggwuggbwwwwuwwbggbbbgb
rbgbwrgrgwrbrwgbwuugbwbuwuugbgggrgbrubugbrurbb
wwwubgbuwugruwbuuuguwwgrwugruurbrbbbrwrgbgubrurgwrwuwgb
uuubrgurgubrwrwbuwwwuwuwbbgwgwwwugrwbwgubw
rwrwurwggurrwburrwwwgrwwrgwwgwbuguwwgrbb
ggurbrrrwbggrwbgbggrbwubwgwbwrubrwugrwgrbbwugubruurwrbur
gbgwwgbwburrububwgrwrbgurwwbwbwguwrwrurbwb
urrrrwbuuuwuwrwbuurrrrbwwrbwgwwwurbgbgurwgubwbwuurrbrww
ruubbbwrrbrrwbwwbwurgbbrrubrwwwwwurwrgwgrwu
wwubugrrbgbwwuubrrrugggbbwbrbbubwuwwubbbwwggurr
bbrgrrwuugrgbuuwgbgwurbubbgbbburggggubrrrrbbugwbrbb
rrgbrwgwuggrgwugrrrurgrrubgrbbwbbwbwwwrbgurbbgwwugrbr
uwrrgwbwruugurrurbwwrbbbwwbubbgrrwurwurbur
gubgrbggruuruwwuurrwrgurwgubugbuwuruwbbwrrwburwbrrwgr
ugwbwgbwgrgwugrwbrgrwrwuwbburwugwuuguwwbrbwrgr
urwrgwbrrwrbrwbugwugwwwrgubgruubgwwbgbwubrrrbbwwb
bbwbrrgwbgururbgrbwbuubwugbwruwubuwbwgbbbubbuwbuguggwugr
rwrwguwwgrguwuuguugrgggrrguwbwgwgwrrgrbrbggubgbr
wbrwwwbgbgrbrbggwwwgubwwuuurrgurgurwbbbwrub
ggbwbgrburggggugrbrrbgwggrgbrwrgwbrbguguuuwrwwbwrbb
bggbuuuubrbwgrbwbrwgbgwuuubuuwwubwrwwgubwubub
rrbgbwwbubrgrurrbruguwgbgbugwbwugwuwuuggwurruwugbrrwr
bwwugurbguurbbubwuwubbwrbwgwruwrgwbgugrwuwbrurbwuwwbgrguug
rgrbggruruuburgubbuuubugrgwrruurwrwrurwbbuwrrru
rrrburrwbuurwrbuurrwuuwrrurgrrgwbwrubuggwr
gbrurubwwrrrbuwuwuurwgrubbbrgwuwrggurwuurbr
brugwgugrgguwwwruburburrbbgwbrrgrwwgrwbggwggguwguwbg
gbrrwggwrgrwbgruruugbrbbrwruuubuwbbggbbbgwwuubrbr
wrbuwwrbwwrbbrbbwruuugugrrubrggrgwwbgrgubuggw
wbburubwgwggwbgwuggbuwubuwurrbggwwgrwuugugwgrgwbrwubwb
uwwwwubgbgugbbbbwbgugbgwgrgwgubwubbwwwgrbu
buwgbuwbbrurbuuggwbbwuwbwgbwrrwgrbbuubwbbrgggwbgbbgbwwuwu
rwwuguuguubwbguguurwuwrruwruwwrubuuuwbrubr
wgguwgwrwruwbwburggbggbwguggwrurrruugwwgwb
bwbrbbgbrgbububugwgrbubrgwbwruwbrbgbguwbgbwrrrgwr
gurwbgwggwurgbuwgrwgwwrwgbbrurgwrbrrbubbgrrgwggwbgurrwwwurbb
gbbwgwggggrrrwbuuwbbgrbwrwrbguurgrwwgrgurguuwrggguwug
rwugwrrgrurruwwubbgwbruurugggugwbbbbbwubgwggr
uugguuburrbuwbruuwbwubwbbrgwgwbbbbwgruggrgbggruurruggwu
bbwruwrrwwwwgwgwbrwuurwruggrbwugugubwwwbrggbbbr
brgggbbwwrubrrbrbugwwbggwrrrgbuwbwwuwgugbbwbrwgrbbu
gwubgwrgwrruwggubgbgrrbubrggwrwubbbuurwrwrg
bbwwbggwwuurrgbrgbgwguubbuwrwubgwruwwrubgubgbggggugrbg
bubrgbbwbbbrugrwbrugrwurbwwuwuurbwbruurrruuuwgbbg
ubbbguuruurbwbwrrrurgwgbgrurrwbwgggrgrrwbbrwbub
grbuuuwgbrbrgrrwwggugburwrbgwbwrrrgbuwuwgwbuuwuruwwuwuwrbg
grgrugggrguuwruruwwrrbburwbwrburuuruwurgrwbuurrbb
ruwbbwgrggguwgurbwbwubbgrwbburbguuwrbrgggwgggwrwggwwr
wbugbrgbrurbubrbuwgguurgwwrgguubwuwggrbwgbgbwbbrbrrg
bbbuuurbwwbwrwuwbbwbrbbgubwwbrgwbwwbwrrbwgurwbr
uwrrwrgwbbrgwbwgrbgrbugwggrrrrbrbgwgbgubwwgwwbgururw
ruuubgurrbuuwwwrrrbbwgubgrrwgwgbgrgrrrbbrbbbgwgugwwu
gurguuubuuuuwurgwwbwuwggggrwwwuuuuwwbbugrrwwwgggbuggurwwwb
uubuurwgbuwgwrgwubgburwwbbrrrrururggwwwwbwuru
grgwbubrgbbuuwubgrgwuwbubuugwrrbrgubrwgrbbrwrbrwbwrbgbu
wgwbrbgbrrurwbrrrgrwurgwbwbbbrgrgwurubbuwgwwrgrbwwwbrgrbb
rwurbwuwbuubggrrgbrbbwwubwwurrgurbggbbwuurwgr
wwbwbwugbrgwgburbgurgrbbwrrrbrrgrubrbwrgrbbuwrwuubwwrbug
grgbgugrwwuwrwgbguwgrrwuuubwrugbwrbbugurwgrwwr
wruggububwruwrruuuurbguuwrgwwwbwrwgurrwgburbbubbgrgwwruru
wwwbwrwbrwgbwwuguuuuuwbbuwrwuuggbwggrgwrurg
grgwugrbrbrbbgrguwbgrrbguugbgburggbgwggbrubrugrguuuww
rgrwwuuwrwwrbrgrrwruubwwbgrgbgrggrggwrbgwrbb
uburwubggwgrrrgubrrwwwwgbubrurrgggwuwruruuwgbuuuuuggwrbgub
ugbuwgguwbwugburuwbbuuwwgurbbgwbgbgggbgbwbguurrgurrgw
wurwuuguurrrgwwgrrgugruuwbwwggbuwwguuguubbbgwu
wrgwbwggwgbggggwwbubwbgubgggggguwrbbgwgbrbbbugrrbruwwgu
gbbgrrbgbgrbgwgbubrrwrwwbwurwguuguuurrggwurguggugrr
wwrrgwgbgrrurguwwurbrbugwwurwwurgbrgbrrgbuwggrbb
bbwuguuugbubuwguruwgwgubwgwgguwuwrwrugbuwwugwuwwwgrb
rbgwwbrwbbrwubbgbrgwgrbbrugburbbguwurbwgugbwbgubgrw
wwrgbwurrwwwguwwuwguwbrwububurgbgguwwbbwrwwurbrrrgrwbbuwgg
ubwgruuwbwbbgwrgwuwuwbwbguwgurgbrrgbuuuwwuwbugrbgbu
wbggwbuuwrrwwwububwbwrwwgwurrwgwurgrgbwuugrwwwr
buubgrruwuwwbuwwwwgwrwubggwrwbbwgugrbruubwr
brrbwurububrugwguwwrwgwgbbrwgbbgbuubrbrurwur
bwbruuuugwrbrgbgwrrrrbbwbbgruwubbugwuwrgwbgwbugrr
grgwuwrguwrbbgwbbggwrwrbbrururrrrbuwgrwwwbburbugg
wgbburrgwburuwugrrurbbrururruwgwbwwbrgrurrgbruburgbru
grburubrrrwruwubgubrgrgugbuuubruwburwbwbgubbbggb
rrubwgbruwwgwrguuwbgbruruwbbbwbgrbwgwgguwgrrurgrgu
rgbgwgbbwbwrbwbwwbwbrbugggurrbwbgwugbrbuuwrbrbgrug
ugwrrwwuruubwbrrgbwuurgbrugbbbwgbubwgrgrgrguuw
wwrrbrbubrwwwwbwgbrrugbubuuuuurbuuwuguugbgwrggrrwuggbwww
ugwwuggugubbbrwbgwwgbbubgwrggugubgbburbb
rrrgrwrgwgurwwrrbuuwbgwbuuurwuwwrwwuwwgbrrgbrrbb
brwubugbuwgrgrrbrrgburwrwbgwurbrrrubbbwbrbwgwguwrgwbrbwg
gbrrgurbwrwwubgugwuwgrrwruubwgrrwrrbwburwrbgurwgbrwrububru
gwwwrgbuwgwbubwrbburuurrbrruwurrwruggwuwbrurrburg
rububwgbwwbugrrgwgwrrburwgrbugbrwrguwwbwburubuubbugrgwbrgrbb
guuwrubbwrwuwbrgbwwbrwuuruwbuwuwggbgbbwwgbrgrg
wrbbrwwrurubrwrubwuburwurburbbgrrurrrwwrbrg
wwwrrgwbwrrbwrbugwgwgbrgwuwgruwggrrubrbgwgrwggu
gbbbbwurbuugwwbgwrrwwwgggrwbwwrwrbrugruwrrbb
rwwrrbburgwuuwgguwwuwwwwwwbgwrrwgwwbgwuwwuugbugbrrwuu
urwbgbugrwgrgugwugbbgugbwwubbbgrubrwgrrgugbguuubugrubwrwbr
bugwbuwuubgwbrrrrgbggbbbrbgwwgwwburgbrrubbrwwurw
uwgrbbbrbbrwrbururrururbbwrbuggbubwbguuugruwgubw
bgwgbgrgrgwwrgbuurwbwgrugbrwrrgurugrugurwwubrgu
bbwwrbbuuuggrurgwubbwurburrurgbrubwrbwgugugbwugrbug
rgbgbubwwrbbrrrbbuggwbgubrrrrwurwuwgwrwuuuwrggbbrbg
uubrgubrgbwbwwbrbgrrbguruggurrgbwrwwbbwugwbruuuruwwgw
wbrrrwrgbuwruwrugurwgwrrrwrbgwwwwbrrwgrugu
ubrbwubgbbbuguuggggbgguwbuwrbbgrwrwruwguwgurubbgbbgwu
ubbggggbggwgwwguwrbwrurrbgwrgugugurugururbruuwwwruu
gwgbbbwgbwurbrwwwrugguugbgbbrgrgugggbuwbubuuuuurrbrwgugrrbb
wrwwrwbuuwrbrrrwugbbrbbrubuwubgbrbwgbwuuwwgwuurgbwr
ruggbgugbrugbrggrbbrbrrugbgruugwbgwuuuuurgggbbbruwugbb
wrrrbuwggggwubugbwugrurbwrwbggrwrgrrgrgwwrwurgbgrg
urgbwwbrbrggurbrguwgbrugbrggrwbrbgrrrbuubgbrguugww
grgugugwgrrwgrugwbwbggurwgbwuggwbwgwgurbwuuugbubrrb
brrurwrbbrruwgwubggubuguuuuubgrurwbgwurbubuurwr
buwugrwuwbrgruuwgrbbubruwbgguubwbwugguuggbugburrbrrugurrrr
wbrguwwuuwrwwrwbrbbwubburwbgbwbbwbbrgruwrwbubuggbwww
wuuurbrrwuwbrgwuwbwrbgurugguuubgrurbrguguwuwuuwgubrbbuu
rrbrwrubguwbbrbubbbbwrgugbbrbubgbgwurbrwbbrgwwur
rgbrbwwurgwrrwugbwrbuurwuwgwubrugburrbwguuwbrbb
bwurbburbwgrrubggbrbwubgugbggbbgubggubuggugurwrguuuuwwwrbb
gwrrubgguuwrurgbbrgrwbruwbbubguurrwrugggwbgrrbbwrwwguu
ggubbbwuuuurbgbbbubwugguubbgrrgwggrggrwggbgrbb
rbwgbrbuguugwrwuubwwwbuubwgrwbguwuubggwrwbguuubgww
rugwrbbbgrwwgrrruubbwgwgurwwuwbwguwwbwgrrrguugrrrr
bburuwwwgurbbuubbgwggbrrrgugurwuggrbbuguuuwuwgrbubr
rugbruuubgbgrwgrurgrubwwgwururubrwugurgbbrubwugbruu
grubrgwggggbwrgbuggwubbgrbrugwwrbwgururwugw
ugwugbggwuurgubbbruubwbwrggwbrgrugwuwwwrgrwguwugwugrugbgbu
rrwgbrgbgrbugwwwrwruruwuwwbubrrguwburbubuwgbgbwwwbgggrb
rubbbugruuguwrwwugwggggbbrbuwurbwrwrbwbrburrubgwuu
gbwuggbrrbgubwuwgwururuwwurggbbggggwwrgwgbb
gwrbruggrbugwbrwuwrbrgurwugbggrgbbggwwrrgrguwubuugrbubrbb
ubbbrurrwuwgbwruwrgwwwuwbwrbbruguubrbbgwgguwbubbgggw
uurubbwrwwrbbgrbrgurwurbgugugurubuwgrbbwwgbbrgguug
gwggubbgwbggggrggbuugruwbuuwwubrbgrwrbbbwbrbbggwgggg
wrubbuwggwrwrbwruwuwwbbrrwwgbgwubwrrwurwgwugubwgguubwubuu
gruwrgbwggburrgugrgruuurrbrwwbgwguwbgrruuwgu
rruuwwrrgruwuuwwruububwuuwbbgruurwgrrurggrrrurrruwbwg
gururubgbgbuuwuwbwwrbggwbbwwwrrbbbbrwgrurwbuwr
wbrrurwuwgbwwwbwbrwbwuuwwggrggrwuuuburgwbb
gbuwgwguwrwwgrrrrwgwbwgbbwbgwbbrbbubwgbuurrgwurrg
gwgwruubbuwguwbrwbbrguwggggwbbgbrwwwgbwbgwwgwbubburwurwwb
wuwbbruubwrrrwguggrbuuubbuwbwbrwbwggbbuggruuuru
rrgbuubbrugbwuuggrgugwbugggguuwbbgbgrrgbwb
ububwwgbbgwbbggwgwgbbwgurbuuugugbuwurbbgwu
gubrbbbbgbgurwugwrggrbgbguubrrgbggugrrgwbwbrgrwrw
wubbbwbgwwuubwwrbggbuwrbbbuuuburbbgugguurwrwwwruu
uguubbwubgrbbwbbbwwgwwgrrwwurbubgrrrrgrwgwgbwggbbrrbgbb
ugwgurbwwgrbbrrugbrwwrbbrrrrgbwbuwgbgrubgrg
urugwwwrbbugubuuwrgrwrwbrwuwgbwbubgwbrbugrrbuggubgubr
uwurbubbrrgwrbbwubgugwwggwggwuugwrbwburgwruw
wwrgggbwwbrwubururrwruuwrubrububrwgwubwbbrwbuwbbgwb
urwggrwggwbwbuwburbwwguggbubbgbgrrwubuuuwwgb
guugrrruwbubwggugugrwwgubgbwbbrbwbgbrwrgrubr
wwrwguurrubggugrwrubggwwuurbguugrbbrburubwgurb
uurgbuuuugrgwgrruwwbbgggwwugbwwwbuubuubgwurwugrrrwgbwurbb
wbubuwgrubwwbbgbbwrrugbrrrrbbwgwugrbggggwrgwbburgwuwbwurg
bguurrwwugbubgurggbugbuugububwrwwwugbbbuurrgwubugubu
uwuwgbubrwubbuurgggburrbuwwwbguwrwurburbbuuru
gubgrrrwgrwugrbrwgggurrbgbrurggrrbuwwuubgrwubuwwbbrbrubu
gburgwurruugrrbwgwgbwwbwbrurrwrugwrrbbgubguugrgbrbu
bgwuuuwbbugbwrrbguuwrgbbrrbrugwbuggwwrrruurbugwguuwubu
brwrgbburrruguugguuugrgwgbugbbuburguggrbb
rugrgwwrgwgrbrwrwrrbwrwbuwggbgwwruruugbbugbrububbbwwruu
wuwbwrubbgbgwbugbubgbbuwubrgbwwbuwbwuwubug
gwwwguwbrgrrrwwwwubguruwgrbgwgbuurwwgbuwbgwwbrrurgwwb
rbwuurrbgrubrugguubgggububbgrgwbwurggbgrrbu
rwwugwurrubrwbrbwwrbwbwuwuubrwwgwuwruwuruwgbggugb
urrbrwbgbbgwrrgrgrurgrbuwgbgwwugurrbrwrrbwbbugwr
bguurgrwwruuggbrrurbrrwrrurwguwwgrwggwbwbbwbrwwrbw
bbguwbrbwuwurrbgwbrgwwwuugbbbbugggwguggwwu
gwgwgurwbrruwbgrrbggugwrwuwrwgruguuwrgrwgwwggguuruwwurbu
rbwuwgwwuuuubwbrubrrrbuwwwuburrwburrrgwurb
guwuubwrgubgwurbbrrrgbbgbgwubrwbwggbrrbgrgrggrbrbwuubrbb
wrwrbbbrrrugbbugrubrrrbggbwrrwbrbbrbrwuugruuwubggwrurubbrr
grgwbrgguwrguuwwrbgugugbrwbbwbbgbwwrrrwguubuguwrwwrbgwg
rwburrwuwgrrrbgurgwbgbbrbuuugwwwuwggwwbwwbgguruwguru
buwwgbbggbbwubwbbguubwwburwbgrbggrrwwuburrbgbubugbbrwb
ugubgubrrurrwuwrrbrwgrgrrbubbgwgrrbrbbrgubgr
bgrbwbgwubrbbruuurwwbrwbuuubrwwrurgbggrguguubbwuur
brrbrbuwubwuwguwbbbgwggbrgwurbgbruwgrrgbggbgwbgwwbgubrgggg
wuwggrwrugubrwbgrwurgwuwgrggwrwguwgbwgwwugbwggwbrrgbrrgg
wwbrbgbruwrurgbgburuwrwubggbbwgburbwrrwbwgrwgr
brguuwrrgwgbguwugrbbrwbbgbubururbgrrrbwwrgggurr
rgbrgggugwrwggwururuwbburwbbbwbuwgubbbbguruwgrw
wwuwgrwgwrwgrurrwbrwwuwrbrgugurrurgurwbrbwuuwgb
grurrruruguuwuguggubggwbwgrbwwwrwbwbbuuuwrwbwggbrruwb
uuugwbwuwrgwuwbrbgbbbgruguwbbgbwgrguuwuguggwu
wwgurrrbbwwbgggrbrwbggugwrbuubwrggrgrubwrrwwwbbw
uwrrwruwubwuwburwrwwgwrguggggbggrwbggwbggugu
bbrggwrrrbrwuwrwwuuwbguwgguggrubwwbgrwbugguggwwubgggubwr
rbbgggbggruwbgubuwwgwuurrubbggbugrgggwrbb
wbrugrwwuuwugbrrwugwrbwrrbbwwrggrwrwuuuggurrbb
uwuwubrgrgurwugbrwrwugggrurgbbrbbbbgbwwbrubw
uwrrrgrrrrrugrwbbwwwbugruuubrgrwggggrgugwguugg
bbwbgrrgwwubuwguurbbguuwrwrgrwuwbbbwuuwgrbuwwrbb
gbuguwugrwubggugguurrrggrbbbbgurbbwugbwgbrugurbgwr
bgrwgbwgwrgrwwrrgbwwrgbbrugubbrrgwbrwgwwbubuwurwgbbrrbwu
bbuubwrwbbruuwubgwrwruubwubbwbbwgwruwbrrggwwwggguwruugrww
uuwwgrrggbrwbgwbrurrwwuwruubrbggrrrbrwbwbbbg
wwburuuuruuubuwuguugbbrgruwurguwburuggwuuubwgwgwwuggug
ugwrwburrgwggwuwrbuggguwgburwwgwbbwbwwgbbbgwg
wgrrgwbbuwwwrgrbgrgbrggwggbwrwgwububbrggbggwrgbwwbgbrbb
rgbbggwgrbwuwbuggrbbguwwbwbguuugrbwuggrrgwrbbr
wwrbrruwgururwwuuuwurbuubuggugbgwrwuwwugbgrbwub
bgbwrggwbwrbgggwgwgrbrggwrgbruwwurbrrwuuburbb
uuuuwrrrwwbwurwubgruuwbrrrguwgggbbuggwrbwbbgwruguwgugugub
uurrbwgwbrwwwubuuubggugwgrburgrrwwbburugwuw
uburwwbggurbwggwbgrbbubwwwuwgrugwgrguugurbrwgrwwugw
gbwbguwbwbrgrubrrbrrrbbbwrwrgwwbggbburrrbwgwgwwwrb
gruwgrwgurbrubrugwbbbburgwwbrgwwwwwgguugwwubrbbuuuurgb
rrggwubbgbubuguubwbrbwwuwbrwurbbgwbwrggrwurwuw
ubugbwwgrgwbbrwwugugwgrgbbbrurwwwbwbwrrruugbgbbgwrugu
bgrggubrbgrubugwrwbwwgrwwrgwbgurwwwbbwrbb
rwbuwuurbrbrwubrwrbuurwubrgrbgwurrbgwbwwrugbrrwu
uggugguuggbguuwubururwgbgwwrbwbuggguwbwwuwugwuwwr
rgrugwrrwwruuuwrwrgubbrwubbbwwggubbgburwgrbwurbugbrbrbbwru
wwggbgbgbrgrbgrbggrgurrwurwrbugubrgrgrurwrbgbrrurwgbwuwubg
uubrgwwggwrggbbwurgurwguwugwurbbuururuuugururwwgrrggggwgrb'''

example_data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''


BLACK = 0
WHITE = 1
RED = 2
GREEN = 3
BLUE = 4
NUMBER_OF_COLORS = 5


def load_data(data):
    sections = data.split('\n\n')
    towels_line = sections[0]
    towels = towels_line.split(', ')

    patterns = []
    for towel in towels:
        patterns.append(read_colors(towel))

    design_section = sections[1]
    design_lines = design_section.split('\n')
    designs = []
    for design_line in design_lines:
        designs.append(read_colors(design_line))
    
    return patterns, designs


color_code = {'b': BLACK, 'w': WHITE, 'r': RED, 'g': GREEN, 'u': BLUE}

def read_colors(s):
    colors = []
    for c in s:
        colors.append(color_code[c])
    
    return colors


def find_patterns(patterns, target_design):
    return has_match(patterns, target_design)


has_match_cache = dict()
def get_has_match_result(design):
    hash = make_hash(design)
    if not hash in has_match_cache.keys():
        return None
    
    return has_match_cache[hash]


def add_has_match_result(design, has_match):
    hash = make_hash(design)
    has_match_cache[hash] = has_match
        

def make_hash(design):
    hash = 0
    for c in design:
        hash = hash * (NUMBER_OF_COLORS + 1)
        hash += c + 1
    
    return hash


def has_match(patterns, target_design):
    cached = get_has_match_result(target_design)
    if cached != None:
        return cached
    
    found = False
    for pattern in patterns:
        if not starts_with_pattern(pattern, target_design):
            continue

        if len(target_design) == len(pattern):
            found = True
            break

        remaining = target_design[len(pattern):]
      
        if has_match(patterns, remaining):
            found = True
            break
        
    add_has_match_result(target_design, found)
    return found


match_count_cache = dict()
def get_cached_match_count(design):
    hash = make_hash(design)
    if not hash in match_count_cache.keys():
        return None
    
    return match_count_cache[hash]


def cache_match_count(design, match_count):
    hash = make_hash(design)
    match_count_cache[hash] = match_count


def count_arrangements(patterns, target_design):
    cached = get_cached_match_count(target_design)
    if cached != None:
        return cached
    
    count = 0
    for pattern in patterns:
        if not starts_with_pattern(pattern, target_design):
            continue

        if len(target_design) == len(pattern):
            count += 1
            continue

        remaining = target_design[len(pattern):]
    
        count += count_arrangements(patterns, remaining)
        
    cache_match_count(target_design, count)
    return count


def starts_with_pattern(pattern, design):
    if len(pattern) > len(design):
        return False
    
    i = 0
    for c in pattern:
        if design[i] != c:
            return False
        
        i += 1
    
    return True


def p1():
    print('part 1')
    patterns, designs = load_data(data)
    # print(patterns)
    # print(designs)

    print(str(len(designs)), ' designs')

    possible = 0
    for i in range(len(designs)):
        design = designs[i]
        print('design ', str(i))
        found = find_patterns(patterns, design)
        if found:
            possible += 1

    print(possible)



def p2():
    print('part 2')
    patterns, designs = load_data(data)
    # print(patterns)
    # print(designs)

    print(str(len(designs)), ' designs')

    count = 0
    for i in range(len(designs)):
        design = designs[i]
        print('design ', str(i))
        count += count_arrangements(patterns, design)


    print(count)


p2()
