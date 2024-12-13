# https://adventofcode.com/2024/day/3

input = '''<;'mul(234,359)who()-who():where()}%what()(when()mul(260,344)}[$*{&from()?]>mul(87,298)what()&+)who()(!#!when()mul(407,173)who(952,771)how()@!?what()]#mul(763,519)'from()$when()%mul(258,409)<)mul(703,155)who()who()<!!mul(423,685)%<?what()how()!,mul(647,758){'mul(595,333)';mul(228,760)~what()@when()who(617,201){{mul(403,912)when()-}(^[^;mul(513,464)where()mul(154,341),$~#^/ mul(469,16)^mul(328,795) from()what()who()when()from()mul(547,469)how()}<?#(/mul(365,823)where();]^^@{(mul(211,19)from()?-+?;@how()where(921,941)mul(816,990)/#)<when():<:'mul(698,62)&~@)+^&$mul(485,158)why()<when(),how()>when()-^}mul(736,421)^<^@?]#;mul(817,275))do()from()how()@where()<@mul(909,873)]:don't()!}&%why(418,225)}-(#mul(212,255)%} ;!]mul(707,897)how()$mul(837,220)when()(,-:+mul(560,935)mul(932,628)when()$&[mul(860,85)&where(){;*:mul(189,383)#'mul(219,523)(who()mul(950,9)';/mul(388,844):~,mul(66,658)where()what()&$&mul(871,390):-mul(587,687)?what()mul(905,131)]what()/+don't()->when()];<select()-where()mul(926,945)'mul(180,934)!don't()mul(736,865)//%mul(662,142)^+>where()'mul(108,216)@?]:mul(222,569)from(961,743):$&-/when()*where()@mul(669,307)$&]who(719,188)>#how()< mul(902,394)when()-^:mul(949,576)@mul(193,521)mul(319,755)?where()mul(494,883)(,>@where(533,792)/mul(579,616)&+?how()~select()mul(840,737)why()-+select()/how(313,74)//where())mul(895,693)from()<don't()mul(984,889),)}who()mul(233,534): ^&~;/<mul(257,146)'( -#!from()]^mul(870,750);select()-how(155,90)why(315,964)mul(298,2)$,how()!@from() #what()#mul(977,312)$&{!who():+$:mul(544,624)from()/mul(404,459)$:?}(@<@what()mul(607,342)who()@how()who()]mul(182,480)'what():@%>*~#mul(410,170){*{where()~~why()}who()mul(796,85)'+&^-)mul(603,101)who()*who()when()@when()where()%/mul(925,329) who()[& ] mul(788,146):^mul(959,154)#{;select(),:^+(from()mul(763,850)/+?mul!,&'what()from())+mul(241,655)>'^/)>why()who();mul(431,988)$from()mul(289,336) &how()what()mul(225,551)when(465,383)&!?['&when() %do()* when()#mul(677,661)what()?mul(688,941),!what(),who()?(who()mul(954,807)!'why()mul(414,536)'who()mul(614,164)mul(941,169){>:mul(755,577)@;!'^@{+mul(640,716)from()from()!where()where(503,241)(&mul(155,305)>([when())select()who(),>,mul(624,695);,what()[]select()!where()who()$mul(100,414)]where()how()!^:who()do())mul(116,506){<%/mul(922,523);why()&mul(850,674)[>^<$;select()what() mul(671,568))why()~?**[*how()mul(920,910)^^-@what()mul(783,710) ]#who():who()mul(492,190):%<how()mul(432,182)[%?mul(758,818)%+!@~mul(241,233)^mul(557,142)^?where()what()why()mul(400,622)%)$mul(251,504){#>+&+(how()#mul(771,755)~mul(709,707)<$[<~}why()[what()[don't()%(^mul(987,332)-]%+]<}who()!mul(144,70)~;*<:mul(218,330);*}what()who()mul(334,779)[@select()where(631,792),)mul(508,632))%;!what()select())>mul(411,371)(?who()select()>?:mul(526,934)mul(804,300)
*+!#-select()where()mul(91,61)$'#&who()where()[,)who()mul(995,486)~(from()]mul(395what()[%from()'%mul(3,116)$-;>why()mul(80,100)don't()+<{mul(40,909){,from()-from()}*mul(5,637)~#don't()>{)#?~mul(710,464)mul(574,738)),'mul(529,787)])how()<who()?*/:#mul(989,869)]how(96,728)+?what()where()])mul(725>,':+<{}mul(805,948)#&!do()#>who()()mul(741,273)mul(183,374)@#{~from()+from()-#mul(155,454)^@#%+<[^{where()mul(24,698)^~!what()don't()^mul(807,271){*;#?&^;from()<mul(210,40):why()*^!$/@mul(392,727)!]:;[?>how()mul(95,214)>select()#~why(152,808)] do()mul(242,354){mul(118,780)<where()mul(237 what()/mul(943,660)mul(238,123)<+}#what()&+where()!mul(850,209):'*select()mul(832,641)mul(374,249) {*{>'@ )?mul(6,158)when()how())[#select()^+<mul(757,651),why()}(#!mul(113,873)-%!mul(157,958):don't()}where()where()why()?!mul(596,489)*from() &&mul(699,920)mul(528,834):^how()+$mul(766,867)*#do()&mul(548,545)(/,*$mul(65,784when(360,503)}from()mul(715,419)what()#/mul(629,49)# who():~mul(362,297)<<from()mul(355,704)>}[;how()[who(101,571)why()><mul(840,568)&,&from()don't()when()mul(706,400)}:'mul(745,820)from(){where()?/!~mul(520,697)*#when()mul(428,711)mul@how():who()*@%];mul(516,414)where()-how()]*;mul(669,963)~from()]select()how()(mul(723,742):,what();}& why(274,391)>mul(791,364)who(683,177);mul(590,613)from()when()why()*:mul(440,124)who(82,539)how()-*%' ,when()&mul(566,425)-;*//(how()<*don't()<%?!{%why()$>mul(37,637)(what()(]<':mul(591how()when()$>$:+#mul(919,784)>*}select()} mul(9,439)';{from()mul(774,58)!%':from()mul(382,161)/when()select(){>#%&mul(434,502)^&/(why()}when()why()from()mul(407,807)'<*{#mul(506,544)],+'[mul(288,577;}>+@who()(mul(684,3)>#mul(878,375){ mul(868,218)why(){mul(738from()+!who()&mul(226,71)from():-where(898,603)/$mul(429,484);}(&-,(]mul(373,23)+,mul)!who()where():;select()how()mul(619,655))mul(572,765)</-mul(422,415)select()how()/)how()mul(691,406);% [what()(from()mul(46,308)$where()'!mul(882,592)when()what(736,407)(why()?(< /-mul(42,917)mul(86,993)~~mul(243,489)*+:from()^who(777,604){[mul(54,523)}mul(675,809)}how();who()mul(52,681)${:who()mul(124,290>?;:&why();%(mul(662,820)from()when()+mul(451,488)* /mul(833,260)'mulwho()#]how()from()*@mul(796,371);{{@^<;~mul(82,742),who()[?:'what()do()@}-}mul(466,182),select()$}{^~how()^mul(263,924)?{??mul(979,300)/:*!mul(85,685)>mul(289,416why()?++$%}{mul(519,250)#&/mul(42,521)what()mul(665,935)where()>~<)who()[mul(457,738)-'$mul(459,702)$;~{;+mul(36,315)mul(881,516)*#$~from()why(967,755)mul(569,650when()>~!:*%&don't()}(^who() ~how()mul(84,748)how()mul(362,548)select()/:%mul(30,445%;;/(}who(971,849)<?^mul(688,9)when()mul(848,69),]mul(109,183)mul(764,444)[(]{[^(mul(505,559)%[mul(470,217)$@select()*why()$ mul(374,21)~what()[}who(); @}mul(387,945)how()),mul(990,737)where(),~*mul(947,938)[mul(603,229)#when()who()*select()mul(852,493)mul(537,342)mul(442,380]],$mul(122,335)
-mul(510,616)mul(235,612><#}who()+?(mul(367,39){};mul(435,762)from()&<?,~select()#where()mul(465,421)'where(608,591)+&when()mul(422,877)$)/#)?{why()(mul(184,55)(select()[&mul(92,651);when()#*[mul(527,555)mul(208,942)({)how()[select()[who()do(){*who()-/$@mul(427,566)where()!&[when() mul(512,215)[select()[where()$how()'where()mul(725,463);#select()don't(),-~+when()%mul(174,734&?mul(929,59)#<what()~$/(mul(184,5)%{}mul(121,138)?where()mul(840,231)}mul(13,563)}?what()why()*>mul(967,363)what()-select()how()!select(),what(){mul(678>what()what()where()mul(32,798)(where(994,20)mul(657,41)when()select(949,914))^mul(790,381)where()mul(854,543)mul(133,378)%how()select()/from()mul(629,798)}mul(371select()do();/where()#''mul(218,299)$^from() ' +why()mul(401,872)!/select()mul(824,807^[mul(992,848)from()%what()when()(-(,mul(453,186)how()who()mul(320,220)who() why()mul(445,909)^>mul(535,611)who()%what()<&mul(760,213){mul(842,923)}'what():when()%where()--do()when()where(732,868)when():why()'why()why(242,296)#from()mulwhen()}{-'>}!why()mul(820,582)~mul(661,206)({don't()select()+when()*:who(544,855)$from()mul(463,28'<](who()mul(851,538)}#]who()who():from()#%mul(320,395)!/when()~$#{+-mul(822,348){)((what()}$mul(396,562)mul(597,851)mul(164,858):!>]mul(421,774)+(mul(302,479)@$mul(393,48 /)}who()@why()+$(mul(94,468))#from()mul(97,244)'?>-how()mul(801,524)+*mul(798,793))!where()~?*mul(803,188) ~when()''mul(276,321(select()do()$&]what()why(224,253)>>$&~mul/*-@'?!mul(273,411)when()-@;why()[when()mul(911,533)!+^how():@from(177,840)@from(951,534)?mul(870,233)from():when()who()where()who()mul(199,165)mul(807,41)what()'~**:mul(487,78)}};mul(392,620)^{why()*<?-when(542,189)mul(531,837)how()]{?mul(798,614)mul(864,588)what(856,979)+~,}select()?&mul(659,85)>who()&(who()~when()#how()!mul(22,783)?select()[&why()select()^mul(671,865)mul(927,45)*#;;how()&mul(519,741)mul(656-what()select()?where()mul(214,386),why()how()mul(924,777)why()%^ &when()what(998,86) [do() -:?how(235,349)%mul(567,616)from()from()mul(665,710)-:*+select()when()[do()[$from()-$%mul(113,895)#-][&when()#where()><do()(!mul(797,837)select()mul(524,378){>%when()mul(914,804)'why(88,694)]]}mul(52,954))why()don't(){[[>@-mul(988,821){],?'how()%:mul(448,457)+ who()?who()mul(62,38)^&>#*?mul(464,719)mul(251,921)mul(82,764)}*#mul(150{+who()+mul(659,141)}select()>why()/mul(270,268)how():mul(523,786);how()+why(685,187)mul(607,577)?(:mul(510+&!&$why()mul(263,702)from(),<^mul(679,458))'/!&do()select()mul(174,946);! :''mul(876,163)%what()/mul(182,358)-+what()^mul(510,134)>select()*who()mul(538,210)from(),how(362,521)@>select()what()who()why()from()mul(525,17)what()(mul(367,947) ?+mul(602,880)^,select():[why()mul(782,143)}]mul(310,79)mul(693,386),mul+~where()];from()?>where()mul(749,859)select() +,^where()mul(611,689)where())!+!!,:mul(486,599)>how()><where()%when()why()>mul(409,246 mul(220,151){select()where()^mul(168,729)>mul(42,222) ;mul(460,16)/({why()}&mul(378,136){@})mul(713,841where()mul(622,542)who()^}#from()mul(975,695)mul?):]mul(65,736)]from()[(,&#who()from()mul(601,954'~*()<;$> mul(332,193)-~when()/[+,/,#!/usr/bin/perl;mul(507@[how()#'where()why()mul(607,129)@where()*'who()~&mul(48,672)
;[?-+(@when(618,593)@mul(463,743)@&when()&~;<&mul(78,96)^]mul(857,303);~/select(),mul(980,536)who();#$mul(223,620){ -(where()mul(960,194)+! [((who()@%mul(530,458)~[?'from()%){%mul(547,623)%(:from(622,543),mul(484,923)why()who()&)mul(261,937)what()#>where()from()[)'mul(342,883)who()$mul(630,484)what()mul(29,250)]'%}when()~!&>mul(995,972)when()mul(15,702)(~#[where()mul(965,454)/,who()mul(739,675)@%-how()-what()*'%mul(810,99)when();[ #mul(22,38)+don't()~[#who()/mul(17,38) why()mul(778,682)how()@?<when()<%mul(695,791)&+%?-where()>[#~mul(780,237)#what()'mul(338,796)$what(825,687),><</how()<]mul(593,291)-:mul(107,558)&from()select() ,how()*[how()mul(811,501)*~(}[{@/,$mul(588,893)--select() ,*mul(291,200)@mul(380,703);~why()how()where()?-how()[mul(746,5),~-mul(271,992)*$*when()mul(626,216)(how()!<how()' how()mul(648,45) {(,what()where(946,541)}#mul(144,262){-#)when()~^mul(515@where()$ +]mul(357,55)^[)mul(404,638){mul(917,462)why()mul(826,942)what()$;][who()what()how()mul(829,811)~what()~when()-)mul(288,652) /who()mul(326,472),))mul(86,683)$/select()/$}where()-)+mul(561,359) '<)mul(304,38)select()>/+@^mul(885,827)?[ why()^when(364,10)>&mul(852,590)^<when()why()why(),~mul(311,677)*mul(707,282)when()mul(19,241)mul~:>/how()%from(699,716)mul(680,396)[!%}select()when(463,111)~who()#mul(363,227why()@,mul(487,707)how()[{+/what()'[}[mul(975,629)>>++{[$mul(336,79):from()mul(707,55)#)select()*<who();mul(602,976)mul(949,866)what()when()mul(72,693)+/$*(from():where()'{mul(202,519)%'mul(773,650)&}[when(): #(&mul;+/!##?why()mul(369,77)from()}#(,]who()>]mul(992,868))where()mul(106,687): $!where()mul(744,983)how()!mul(313,790)(+))]select()*!>:mul(210,868)+;why(672,934)how()when()why()>%]/mul(108,885)&/{how()mul(159,898),()who(),when()?<#mul(188,958):from(636,533)+&<*[select()how()mul(152,658)who()*;mul(477,718)when(720,25)!who(){&mul(795,952)select(435,575);!/how()select()^select()mul(281,344)from()$<>*:!mul(830,180))(select()how():&mul(397,50)*mul(413,309)where()~,/,mul(796,87)*<~&!(&don't()select()( what(709,443) &who()']mul(445,518)^:mul(655,75){from()mul(377,846)where()mul(321,815)mulfrom()>mul(937,444)where()?}how()mul(112,471)what()>%when()where()who()<$mul(318,492)-what()mul(78,20)select()?mul(851,874)&!#;select():?'^*mul(598,757)mul(326,573){/[%,why();mul(445,682'(who()^+why()why()from()mul(816,284)*%&^'^)>mul(274,211)@*,'^(mul(592,927) ;!~&how()~mul(195,155)mul(896,831)what()()+#who()&*mul(708,134}^who()where()&[mul(138,384)+select()who();where()-?&[mul(767,907)*mul(436,412);[;)-{#(where()mul(987,536)don't()#?mul(616,255)+]:when()when()}#mul(41,533)#^>from()<how(290,301)mul(63,747)what()(+;^,#who()how():mul(249,969)select()+ mul(387,732):+{what()~:!select(67,813)mul(788}!;:*where()<mul(291,542)why()('^&where()]/how()&mul(605,763)-]-why(),@mul(556,282)how()'>!what()mul(151,867);/]select(),mul(754,334)&:mul(97,118)select()mul(593,702)
&*don't()]select()from()where()[mulwhen()^^/from()&mul(461,659)&mul(643[mul(572,503)mul(588,137){;mul(849,301)who()how()%;why()who()mul(233,687) why()*do()+who(),#how()( -mul(650,3)^+mul(14,551)who()^#? !<from()]mul(912,640)!?where()*%mul(328,45)/how();;where()(mul(843,155)who()what())?%what()what()@mul(923,667)) @how())+who()-mul(503,43)when(530,489)why()from()&select(617,173)what()mul(471,175>~>-mul(628,710)%;why()<('$&:when()mul;why(155,340):^+where()/[%@mul(931,55)%(~:why()from()mul(715,482)!{mul(766,239)how()mul(284,603)>where(897,837)mul(530,610),;-why()<select()/]!mul(389,108)'[~#mul(230,503)^)%~^how()^(&mul(216,268):mul(190,552$</who()!select()]do()}what()mul(144,685)%(don't()/[where(),>^}select()(mul(470,194)from()*,who()!mul(394,768):from()?{$ ;@~mul(571,519) what()[:mul(65,328)where()>~where()< :#mul(490,774)'why()>,@<mul(945,164)?,select()from()]mul(191,618);') #mul(984,94)^^mul(764,343)[!~?%why()-select()mul(802,97)#why()when()~,<?mul(817,989)![>mul(588who()}!-'mul(35,602)+ -%[' how()]:mul(502,722):why()!!mul(332,723)!{ ,[}{^who()don't()&@[when()>'mul(695,738)select()how()do()what(635,547)};>mul(50,148),,,mul(974,330)mul(973,477)+>mul/<how()why()])[+where()mul(727,316)&}#*];(~+do()>when()mul(74,42),how()who():,what(182,526)>mul(301,319)from()*how()#mul(808,632)don't()%- ~mul(671,835)who()}&mul(330,88)){+when()&who()<$who()where()mul(653,324))(select(){/!*select())<mul(933,167)/::?+~*how()mul(266,2):**!)what()mul(491,655)}?mul(949,984)~(,who()%mul(254,681)who()%from()-;from()?%{)do() [{mul(570,36)):^;{-who()<mul(820,352)/,>select()mul(800,74)mul(780>~where()[)/why():+mul(95,301)+#~-]^<  mul(453,169))!)-who()}select()!/+mul(514,816)'>,)mul(188,237)'(*><<who()why())how()mul(738,289)what(639,365)$</]~'}what()when()mul(102,510)mul?!/%why()-why()who()where()how()don't()who()who()&',~%*where()mul(790,751)@;]mul(699,591)from(10,889)'from();~?%'mul(501,173)):mul(92,868)~>#@from()$&[mul(896,181)+why()[/}mul(292,818):what(933,189)when()where()+when(),how()mul(325,460)*!'?$}why()mul(868,19)]>do()]]'@-select()+?:,mul(705,664)why() :when(320,386):]where()mul(101,603)from()mul(584,674){*why()mul(527,341)mul(314,923),&*!#don't()from(),&: mul(610,911))(!when(12,857)how()&}/don't(){from(872,604)[]}}$when()from(393,26)mulwhy()why()from():;] }mul(618,762)who()>#' <-@why()#mul(342,769)#'-&<:from():>*mul(995,557)[':&when()&don't()%+}:who(699,463)}?mul(949,652):why()#'what()mul(466,912)how() ~where(){?mul(498,589)-:]}*(<?&mul(922,310)mul(469,882when()who()#{mul(553,266)!;&(%select()?#@how()mul(84,210)from()where():mul(7,362)~?{$~!:why()^mul(770,657)]%#mul(601,370)how()?#mul(81,96);who(){mul(519,362)what()} ##:~>mul(554,92)select();~how()&#mul(296,200)$why()why()don't()mul(718,92)[select()*?:where()mul(868,217)when()'what()]mul(608,255how():*~when()!:%{how(720,870)mul(857,876)+[how()select():[mul(926,987)why()]select()don't()%?,/&][]>^mul(20,520)mul(970,495); ?from(971,165)+@'{>mul(541,168)mul(697,290)/mul(724,20)/@/how()when()select()(]why()do()-(mul(250,857)}~<mul(670,830):mul(37,452)#%</who()@why()mul(258,824)'-^+#}how(683,511)from()who()mul(572,263))(mul(516,90)&# }where(161,891)$?>mul(612,107):>'}+{(@<mul(410,789)'@mul(41,356)
how()who()from()why()&+'what()+mul(948,970)how()^^ what()what()mul(124,952)#?why()']?when()mul(559where()$/<}#mul(683,315),{*mul(835,821)@%{who()?mul(528,442)#{/+!#>&?mul(264,859):'{;+]who()-mul(671,460)}how()when()[{mul(383,254) !mul(3,918)mul(874,303)!@mul(279,457)why()*>from()do()#/?<mul(522,927)what()[)what()~~how()when()}>mul(567,487)<what()?,][*}mul(390,810)![why()$who()mul(632,35):~ ',mul(741,335)[how()+>]*&don't()(who()}'mul(522,610)when()${{]#'mul(311,306);{^{ '[mul(270,712)@'}%why()#~:^what()do()>mul(6,137);from()-*%,;~<mul(123,497)mul(47,167>how();+ from()[?&how()]do()~who())& &;%why()why()mul(742,979)$}#,what(609,482)^mul(506,252) -:what(362,209) who()mul(399,346)%'&?mul(229,623)!)how()~mul(436,283)!)@how(){?mul(237,965) #>mul(594,38)^-mul(516,90)who(441,355)[+from()/how()mul~%[mul(434,408)where(690,778)when(978,434)>]?what()[mul(907,397)?@do()?@,select()who()-%(]where()mul(36,78)(:+when()select()mul(477,631)[#when()}mul(45,264@who()select()(mul(656,657)]select()how()[))from()mul(444,181)]!+select(36,597){*who()!/ mul(543,648)from()from()from()$when()+-} mul(293,90)who(183,746)mul(872,855how()[!>~from()*?'<mul(449,852)$:why()!+mul(71,240)?@#}:where()+from(){mul(191,72)@&^&({from()mul(981,127)?&how()[}mul(78,213)*&where()when()^what()@&%mul(149,819)@why()from(376,630) when()+don't()(><] mul(664,827)'-from()#*]mul(912,740)'from()when(473,160)mul(459,94);do()?:, ],{mul(322,110)}>where()}when()when()mul(443,449)where()#}~]mul(94,385)where()>do()<*:@##?what()'mul(63,18)[mul(414,464)>do()what(858,375)%}<'^!*mul(855,863)(mul(557,951)select()$what()+?%/ ]mul(805,186)^who()'mul(549,457)mul(604,658)select()!*~mul(508,395)where()+~]^mul(404,113)*)&$-'where()mul(428,314)$($(%$/,?where()mul(33,256)?mul(199,365)&select()when()>what(111,916)from()mul(588,754)(},@-+who()when()mul(828,506)&select(),select()who()#mul(689,772)$-&@+~what()mul(96,741)}?{-where()when(891,721)~do()*#<%who()^&;#how()mul(365,858)*$mul(903,693)who(385,109)what()'%}'mul(27,403)who()mul(874,113)( ,-@@mul(260,787)@why()*from()mul(679,437)?why()from()-what()mul(240,527):,from()>#[$do()}what()]mul(632,184)&)[?when()mul(70,409):[^-where(585,55)]%^mul(779,948)?$}from();[+?mul(964,869)-?^when() [ mul(729,356)how()({>]+ why()how(908,783)from()mul(774,617)!how()')*;]mul(484,579),#select()&why()mul(873,5)(/(@mul(573,802)what()<(<*mul(759,343)?mul(301,853)when()][) don't()?+from()mul(556,868)?$how()@>*when()<:$don't()/<^)/what()!mul(434,251)mul(882,866),mul(744,572)(why(112,504)$-how()mul(154,96)mul(201,94)$[:@&%-,>!mul(188,433)!*?mul(546,999)%&@>*/mul(310,391)-<+{]mul(938,579)+,@%[why()why(75,712)+from():mul(472,593)^mul(733,69)why())mul(961,406)~@$* )-from()mul(932,700): %!mul(382,321)!mul(297,196)where()mul(444,227)what()where())^#who()from()-mul(65,99)$:why()mul(652,486)mul(446,486)mul(970,630)$~]mul(510,304)]*:>how()/}$'''

example_input = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''


START = 0
M = 1
U = 2
L = 3
OPEN_MUL = 4
ARG1_DIGIT1 = 5
ARG1_DIGIT2 = 6
ARG1_DIGIT3 = 7
COMMA = 8
ARG2_DIGIT1 = 9
ARG2_DIGIT2 = 10
ARG2_DIGIT3 = 11
D = 12
O = 13
OPEN_DO = 14
N = 15
APOS = 16
T = 17
OPEN_DONT = 18



def parse_input(input):
    muls = []
    data = (None, None, None, True)
    state = START
    for s in input:
        if state == START:
            state, data = from_start(s, data)
        elif state == M:
            state, data = from_m(s, data)
        elif state == U:
            state, data = from_u(s, data)
        elif state == L:
            state, data = from_l(s, data)
        elif state == OPEN_MUL:
            state, data = from_open_mul(s, data)
        elif state == ARG1_DIGIT1:
            state, data = from_arg1_digit1(s, data)
        elif state == ARG1_DIGIT2:
            state, data = from_arg1_digit2(s, data)
        elif state == ARG1_DIGIT3:
            state, data = from_arg1_digit3(s, data)
        elif state == COMMA:
            state, data = from_comma(s, data)
        elif state == ARG2_DIGIT1:
            state, data = from_arg2_digit1(s, data)
            if data[0] != None and data[1] != None:
                if data[3]:
                    first = int(data[0])
                    second = int(data[1])
                    muls.append((first, second))
                data = (None, None, None, data[3])
        elif state == ARG2_DIGIT2:
            state, data = from_arg2_digit2(s, data)
            if data[0] != None and data[1] != None:
                if data[3]:
                    first = int(data[0])
                    second = int(data[1])
                    muls.append((first, second))
                data = (None, None, None, data[3])
        elif state == ARG2_DIGIT3:
            state, data = from_arg2_digit3(s, data)
            if data[0] != None and data[1] != None:
                if data[3]:
                    first = int(data[0])
                    second = int(data[1])
                    muls.append((first, second))
                data = (None, None, None, data[3])
        elif state == D:
            state, data = from_d(s, data)
        elif state == O:
            state, data = from_o(s, data)
        elif state == OPEN_DO:
            state, data = from_open_do(s, data)
        elif state == N:
            state, data = from_n(s, data)
        elif state == APOS:
            state, data = from_apos(s, data)
        elif state == T:
            state, data = from_t(s, data)
        elif state == OPEN_DONT:
            state, data = from_open_dont(s, data)
            if state == START:
                enabled = False
    return muls


def from_start(s, data):
    state = None
    if s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_m(s, data):
    state = None
    if s == 'u':
        state = U
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_u(s, data):
    state = None
    if s == 'l':
        state = L
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_l(s, data):
    state = None
    if s == '(':
        state = OPEN_MUL
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_open_mul(s, data):
    state = None
    if s.isdigit():
        state = ARG1_DIGIT1
        data = (None, None, s, data[3])
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_arg1_digit1(s, data):
    state = None
    if s.isdigit():
        state = ARG1_DIGIT2
        data = (None, None, data[2] + s, data[3])
    elif s == ',':
        state = COMMA
        data = (data[2], None, None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_arg1_digit2(s, data):
    state = None
    if s.isdigit():
        state = ARG1_DIGIT3
        data = (None, None, data[2] + s, data[3])
    elif s == ',':
        state = COMMA
        data = (data[2], None, None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_arg1_digit3(s, data):
    state = None
    if s == ',':
        state = COMMA
        data = (data[2], None, None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_comma(s, data):
    state = None
    if s.isdigit():
        state = ARG2_DIGIT1
        data = (data[0], None, s, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_arg2_digit1(s, data):
    state = None
    if s.isdigit():
        state = ARG2_DIGIT2
        data = (data[0], None, data[2] + s, data[3])
    elif s == ')':
        state = START
        data = (data[0], data[2], None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_arg2_digit2(s, data):
    state = None
    if s.isdigit():
        state = ARG2_DIGIT3
        data = (data[0], None, data[2] + s, data[3])
    elif s == ')':
        state = START
        data = (data[0], data[2], None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_arg2_digit3(s, data):
    state = None
    if s == ')':
        state = START
        data = (data[0], data[2], None, data[3])
    elif s == 'm':
        state = M
        data = (None, None, None, data[3])
    elif s == 'd':
        state = D
        data = (None, None, None, data[3])
    else:
        state = START
        data = (None, None, None, data[3])

    return state, data


def from_d(s, data):
    state = None
    if s == 'o':
        state = O
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_o(s, data):
    state = None
    if s == '(':
        state = OPEN_DO
    elif s == 'n':
        state = N
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_open_do(s, data):
    state = None
    if s == ')':
        state = START
        data = (None, None, None, True)
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_n(s, data):
    state = None
    if s == "'":
        state = APOS
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_apos(s, data):
    state = None
    if s == 't':
        state = T
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_t(s, data):
    state = None
    if s == '(':
        state = OPEN_DONT
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data


def from_open_dont(s, data):
    state = None
    if s == ')':
        state = START
        data = (None, None, None, False)
    elif s == 'm':
        state = M
    elif s == 'd':
        state = D
    else:
        state = START

    return state, data




muls = parse_input(input)
sum = 0
for mul in muls:
    sum += mul[0] * mul[1]

print(sum)

# NOTE the answer to part 1 is 161 for the example_input
