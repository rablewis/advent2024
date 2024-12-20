# https://adventofcode.com/2024/day/4

input = '''AXSASXXMASAMXMXSASMMXMSAMXMXXMASMXMXMSMSMXMAXMSMSMSMXXMXMXMASXMASXMXSXSASXSXSSSSSSMSSMXMAASAMXXSSSMMXMMMSXSAXMASXMMXSXMAXSAMXAMXXMASMMXXSAXS
SXXAAMAXMAXMAAAXXMAXAXSMXAMMMMSMMMMAMAMAMSMSMXAAAAASAMMAMXMASAMXMASXSAMXMAAAMAAAAXXAAMSSMXMAXMAMAAXSASAAMMAMSAAXSASASASAMXSXMXSAMMAMAMSSMSAA
XXMMMAMMXMMSSMSSXXAMSMMMSMSAMXASAAMAXAMAMAAAASMSMSMSXASASMSASXMASXSAMSMAMAMSMMMMMMMXSMAASMSSMAAMMMMSASMSMSSMSMSSSXMXSAMXSAMMMAMXMXAXAMXAAMMM
XMXAAXXMASAAAAAMMSMMXAAAAASXSSMSSSMSMSXXSMMMXXAAAMAMXMSASAMASASXSAMXMASXMMXMASAMXXAAMMMMMXAAXSXMMMAMXMAXAAAAXAXAMASAMXMAMAMAMXXAAXMSSSSMMMXM
XSXSMSMMAXXSMMMSMAAMSSMMMMMMMMXMAMAXXXAXSMMSXMSMSMSSSXMAMXMAMMXXMXMMXXAMXSASXMAMXMMXXAMSSMSMMXASXMSSSMAMMMMXMXMASAMXXAMXSXSSMMSSMSAAAMXSAXAM
MMMXAAAMMXAMXSASXSSMMAMXXSASAMAMAMSMAMAMXAAAAAMAXAMAASMMMSMASXMAMASAMSMSASASXMXMAMXMMMMAXAMAMMMMAAMAMMXMXXXSMAXXMAMMSSMAMXXAAAMAAMMASMMAMMMS
AAAMMMSMSAXXAMAXAMMMSXMMASXMASXMSAMXMAMMSMMSSSMAMAMMSAMAAAMAMAXAXAXXXAAMAMXMAXSSMXAXASMMSXXAMMASMMMAMSMSMXAXSMSMSAMXAAMAXMMMMSXMXMAAAAXMSSMM
SMXXXXAAXMMMSMMMSMSASXMMMMSSMMXAMXXAXAXMXSAAMAMMMAMXMAXMSSMSSMXXMMSSSMSMXMAMAMMAASMMXXAXAMSMMMAXXMSXXAAAAXMMSMAMMMSMSSMSASXXAMMSXAMXSXMXAAAX
XMMSSMMAMMAAAAASMMMAMAXXAAAMAASMMXSMSMSAAMMSSSMSMASXSXMMXAAMAMSASAAAAAXMASXMSASMMMAASMMMAMSAAMSSSMMSSMSMXXAMXMAMSAAAAAAMAMXSXSAMMMSMMMSMSSMM
XMAAAASXMSASMSMSAAMMMMMMMMSSMMMASMAMAAAMXSAXAAAMSAMMMMMMMMAMAMSAMMXSMMMSASAMXMXMAMMMMASMXAMMSMXAAXAAXXXAMSXMAMAXASXSXMMMSMXXAMMMAMAASAMXXAAX
XMMXXMMMMMMMAMASMMSMSAAXSAMAAASAMSAMMSMSMMMSMMXMMMXAAAAAMXSMXMMSMAMMAMXMXMMMXMMXAXAXSXMAMSAAXMMSMMMSSSMSMAASXSSMMMMMMASAXSSMSMSMXSASMSSSSSMM
XMSSSMSAAAAMAMAMAXAASMXXMAMSMMMAXMXSXMXXAAMAXXXMASMSSSSXSAXMSAAAMAXSAMSMXSXSXAAMMSMMAMXXAXMSSMAMASXXAMXXMSMMAAAXXXSAAXMAMAXAMASAXAXMMXMAMMAM
MXAAMASXSSSSXMSSMMMAMXSSSXMASAMXMMSMMMSSSMSMSXMSAXMAAAAAMAMAXMSMSAXSAMASAAAXMMXSAAXASXMXSXMXAMXSAMSMMMMXXMMXMXMMMMMMSMMXSMMSMAMAXXSMXSMMMMAM
ASMMMMMXMAMXAAXAAXXAMMXMAMSAMXMASXAAAAAMXMAXMAXMMSMMMMMMMXMXMMXAMXAMAMASMMMMXAAMXSMMXSASMMSSXMMMAXXMAAXMXMSAMASXMAAXMASAAXMAMXMXSAMXAXMXXMAS
XXAXSAMXMMMSMMXMMSMMSSSMSMMASMSASXSMMXMXXXAMXMXXSAMXMXXMSSXMASMXMXMMMMAMAXAXMAMSAMAXAMMAAXXMMSMMSMMSSXMMAMMASASASXMSXAMASMXMSAAAMMMMMSMASAMM
SSSMAAMXSAAXASXSAXAXAASAMXSAMXMXXAXMSSSMSSSMMAMXSXSASXAMAMAMMMASXXSAXSMSMMXMASXMAMAMXSSSSMXAAAMAXAMXXSSMASXMMASAMXASMMMMMXAXSMSAMXSAMXMAXAXM
AAMMSXMASMMSAMXMASXMMMMMMXMXSXAAMSMMXAAAAAAMAXMASMSAXSAMXMAMAXMAAAMAMAAAXMAXAMXXSSMMAAAAAXXMMSSXXAMXMAMSAMAMMAMMMMAMAMSMASXMSXMXMXMAMMMXXAMS
MXMAMAMAMSAMXMXXMMMASXSSXXMSMMMXMXAMMSMMMSMMSAMXXAMXMXXMMSMSMSAMXMAMMMSMSSMMASAMMAMMXSMSMMMSAMXMSSMMAXMMXSXMMXSASMMSMMAMAXAMXASMXASAMSASXSXX
XXMSSMMMMAXMASMMSASXMAAXXXXAAAXMXSAMMXMXMAMMAAMASXMXXMAMAAXXAAXMXXAXAXAAXAASAMAXSAMSAMXAAAAMXSXXAXAXSMMMMMASXMSASXAAASXMMMMMMMMAXMASXMASAMXM
SMMAAMSSMMMSASAASAMMMMMMMMSMSMSMAMMMXAMXSASXSSMAAAMAAMSMSSSMMMMMMSASMSMSMMXMASXMMXMXAMMSSMSSMMMMMSMMAAAAASAMXAMSMMMSXMAMAAXAMXXMMXMAXMSMMMSX
SAAMSMAAAAMMSSMMMAMMXAXAAAAXAXAMXSASMSMXSASAAXMXXAMXSAAAAAAAXXXAAXAAAAMMMXXXXAMXXSAXMSAMAAAMAAXMXAASXSSSXMASMMMAXSAMXSMMSXXAXASAXXXSMXXSAAAM
SSMMMMSSMSSXAMAASXMXXXSMSSSSSSMSMAMXAMXMMSMMMMMMSSMAXMMMMSMMMSSMXSAMXMXSMSMMMASMMMASAMASMMMXXMMMSSMMAXAMXSMAMASMSMASAMXMAASMMAAMSSMMSMAMMMSA
XASXAAMMAMXMAMMMXMAMXMSAMAAAXXXAAAXMSMAMMXSAMAMXAASAMXSAXAMAXXXAMAXMMSAMMAAMSMMAAAMMASMMAMXSXSAMXMMMMMSMMSMASXMMAMAMMMAMXMASMXMXAASAAMSMMAMM
SAMSMMSMAMAMMSXMSAXSAAMAMMMMMSMSMSXAAMAMAAXMXAMMXXMMSASASMSSSMMAMMSAAMASXSSMAXSSMMXMXMMMXSAAMSXMAMXSAAXXAXMAMMXMXMXSXSXSAMXAMAMMAAMXSAAAMSSX
MAMXSAMMXSXSASXAXXMXMMSSMXXASAAMMMMSMSSSMSSSSSSMSAMAMXMASXAMAAAXAXXMXMAMMXMMAMXAMMXASMSMAMMSMMXMXSASMSSMMXMMSMSMSAXSAMASXSMMASXMSSSXXXSSMMXM
SXMASXSAXXXMASMMMMMXSAMAXMSMSMSMAXAMAAAXAXAAAAAASAMMXSMAMMMSSMMMSAMSMMSSSMSSSMSMSMSAMAAMXSAMXXSAMMAMAMXAXSMMAXAAAXMMAMMMMSAXAMAMAAXASAMXMXMA
AAMXXXMAMSAMXMAAAAXAMAMMMASASAXMXSXMMMXMSMMMMMMMMAASASMSMSXMASXAXAAAAAAAXAMAAAXXAAMAMSMMMMMSMAMAXXXMAMXSMAXSMMMSMSMSMMSAASMMASAMMSMXMXMAXMAS
SMSSMXXAMMAMXSMSSSMSSSMXMSMMMMXMXMASMSMAAAAXMAXAXXXMASAMAAXSAMMMSXSSSMMSMSMSMSMMMSMAMAAAAAXXMXSSMMMSXSAMAXMASXAAAAAAAAXMXMASASASAMXSXMMXSMSX
XMAXXASMSXXMASMAMMAXAXMAXAXAAAAAXMXMAAMSMXAXXAMSXSXMAMAMSMMMMMSAMXAAAXXMAAAAAAXSXXMASXSMMSMXMXMMAAAMASMXSXAASMMMSMMMSASMSSMMASAMASAXAXXASMAX
SMSSMMSAAXMSAMMAMXMMSMXMMMSSMSMSSXSXMXMXASASMMAMAMXMAXAMXXAMAAMASMMMMASMSMSMSMSMMMXXSMMMXAXAMAMXMMSMAMXAMASMMASAMMSMAXXAAMXMAMAMXMMSMMMAXAMS
SAAAAAMXMSXMASXXXAXSXMASAXXMAXXXMAMAMSXMAAAXASAMAMASMSSSSSSXMAXAXAXMMAMXAAAAMXAAAAAMXMAXSASMSMMAASXMASMMMAMXMASASAAXXXMMMMXMXMAMAXMMMASMSMMS
MAMSMMXAMMXMSMAMSMMSASASMSSXSXAMMAMAMAAMXMASAMXMAMXAXAAAAAAAMMMSXMMAMASMMSMSMMSSMSSMAMAMSASAAAMSSMASASAMSSSXSXMAMXMMMMASAMMMSMMXMSMXSASXAXAX
XAXXXAMMXAASAMXAASASXMASAAMXMXMAMAXMMSSMAXMAXMMSSSXXMSMMMMSMMAAMASXMSMMXAXMMAXMAXAAMSMSMMAMMMSXMAMAMXXAMAAXXMXMASMXAXSAMXSAAMMSSMMMAMASMMMXS
SMSXMSSMASXSSMXSAXXXXMXMMMSAMAXXSMXMMXXMAXSXSXAAMAMMXAXAXXAAXMMSMMAMXMSMXMASXMSSMXXMAXXXMMMXMMAMAMSSMSSMXSMMMXXAMAMSXMASAMMMSAAAAASASASAASXA
XMAMAMAAXMAXASAMXMXSMSAMMAMAXAXMAMAASAMXSXXAMMMMSMMASMSMSMMSMAMXXSXMAMMAAMAMAAAXMSSSMSASMASASXSMMXMAMAXASAMXAMMMMSMXASMMMXSAMMSSSMSASXSXMSAM
AMASMSAMMSXSXSXASMAAASASMMSMMAXSAMSSMAMAMMMMMAXMAXAMAXAMAXAMXXAMMMMMAMMSSMSSMMMMAAXAMMMXSMSASAAAXSSMMXSXSAXXAXAMAXASAMSXXAMAXXAAXXMAMMMMMXAS
XSAMXSXSXXAMASMXAMXSASAMAAAXXAMMSMXMMXMAXAAMAAMSXMMSSMMMASMSMSMAAAAMSXXAMXMAMMSSMSSXXAXMMXMAMXMSMMAASMMASMMMSSMSAXAMSMMXMXSAMMMSMMSAMAMAMSMA
XMASMXAXMMAMAXMSSMMMXMAMMMSSMASAAMAMMASMSSSMMSMSAMXAMASMXSAAASXMSXSMMXMAMAXAMAAAMAXASMMAMSMSASAXASXMMAMAMAXAMAMMASMMXMASAAMAMXSXMASMSSSXXAAM
MSMMAMXMMSAMXXXAAMAMASMMMMAMXAMXMSASXMSXAMAAAXAMXSMMSAMMAMXMSMAMMMXXXAMSSMMSSMSSMMMMMMASXMAXAMSSXMXMSMMASAMXXAMXAAAMXXXMAMSAMMXMMMSAAAMMMXSX
MASMMXAAASASAMMSSMMMASMAAMASMSMXXMASAASMMSXMMMAMAXAXMASMAXSMXMXMXAXMSSMMAMAAAMAXMXMXAAMXAMAMXSXXXAXMASXXSMAMSMMMMSSMSXMMMASMSAMXSAMMMSMAXSMX
SAMSAXSMMMAMXMAMAAXMASXSSSXSXMMASMASMMMSXAXMSSSMSSMMXAMMMMSAMASXMSAAAXAXAMMSMMSSMAMSASXSXMXSXAXMAXMMAXSAMXXMAAXXXMMXXAAXXAMXMMMAMASAMXMXSAAX
MASMMXXAMXSMSMSSMMXSXMAMMAMXAMSAXXAMAXAMMMSMAXMAMMXAMSSMXAMXMXMAAXMMMSMMSSXMMXMAMAXAMXAMXXAMXMXMASMXAXAMXMSSSXMMXAXSSSMSMSXMXAMMSAMAXMASMMMM
MSMAXSXXXAAAAAAMMXAMMAMSMSSMMMMSSMMSSMSXSAAMMMMSMMMSMMAAMSMSMMMMMMMXMAAAXXAMXAMAMSSMMMSSSMXSAMAXXAAMSMMMMXXAMXASMMMAAAAXAAASMMSXAXSXMAXAMXSX
MAXAMXMMMSXSMMMMSMAMMAXSAASAMXAAMAMAAAXAMXMMMAXAAXSMASMMXMAXAAAAMAXAMSMMSMSMSXSASASAAXAAAAXXMXMMSAMXXAAXXXMAMMXMAASMSMMMSMXMAASMAMXMASAMXAXS
SMSXMAAXXAAMMSAAASAMSMSXMMSXMMMXSXMXSXMMMXSSXSMSXMASAMAXAMXMASMSMXSMXAMAMAMAAASXMASXMMMSMSMXSAMXAXXASXMMMSMAMMSSSMSXMAMXAXAXMMMAMAXAAXMXMASA
XMAMSASXMMSXASMSMMMXAXMASXMAXXMASXMAXXMXAXXAAXAXSSXMMSSMMMAMXMXXXXMXSASXMAMMMXMAMXMAMSMMAMXASASXMXMASXAMAAXASXAAXAMMMAMSMSSXMASXMXAMXSXMSXMM
XMXMXAXXXMXMMMAMAMXSMXXAMASAMXMASAMASAMXASMMMMAMAMXAAAXAASASXMASXMMASMMMSMSXXASXMXSMMSAMAMMMSAMMXAXAMXMMSSSXSXMMMSMAXMXMAAAASASMSAMXMAMAAAMX
SMMMMMMSXSAMXAMMAMAMXSMAMAMXAXMASAMAMXMAMXMASMMMAMSMMXSSMSMSAAMXMAMAXAXAXXMASMSASXAXASMMASAAMAMSSXSASMMAMXAMMMXXAXMSAMAMMMSMMASAMXXXXXASMSMM
XXAAAAASMMMSMMSSSMXSASMSMSMMMMMMSAMMSMXAXMXAMAXMXXMAXAMXASASAMMMSSMMSSMSMMSAMMSAMMAMXSASXMMXXXMAAMSAXASXSMXAASAMXSAMXSASAXAMMMMAXMXMSAAMAAAA
SSSSXMXSAASXAXAMXAAMXMAMAAMAMSAMXXMMAXSXSMMSXXMMMMSAMSSMXMASXAMXAAAAAAAAXAAASAMXMSMXMSMMSSXSMAMMMMMMMMAAAXXSASAXSMMXXSXSXSXMASMMMMAMXMXMXMMS
AAAAXMXSXMXMSMMSMSMMMMAMXMMAXSAMXXMSMMXMAXAXASXSAAMAXXAMXMXMASMMSSMMSSSMMSSSMAXMXAAAXMMASMAMSAMAMSXSAXMMMMMMASMMXMXMMSXMASAMASAAASASAMXSSMMX
MMMSMSASXSXAXXXAMXAAXMXSAMMSXXAAMXXAMXMXMMSSMAASMXSMMXSAMMAMXMXAMAMXAAAXAXXXMSMASMSMSAMXMMXMAXMASMASXSXSAAXMXMXAMMAAAMASMMSMMSXMMSXSASAMXMAM
XXXAAMAMAMASMMSMXSSMMSAMXMAXXAMXAMSSSSMXXAAMXMXMAASAMXMASAMSMSXMSAMXMXMMSMXSMMAXMAMXSXMAXSSMASXMMMXMAXAXSMMSAMXMAMXSMSAMAAXMXSMMMSASAMMMMXAS
XXMMSMXMSMAMAMAXMAAMAMMXAMXSSSSSSXAAAAXMMMMSAXMAMXSAMMSAMMXSAMMMMXSASMXMXMAAAASMMAMAMAMSSMAMASASXSMXSMSMMXXSASMSSMAXAMXSMMXSAMASXMAMSMAASMMS
XMXMAXAAXMAMXSAMMSMSSMMSASMXAAAAXMMMSMMXASXSXSAAXMMXMAMASXAMAMMAMMAAAXASAMXSXMMXMXSMMAMXAMXMASAMAXXMXAXAXMASXMAAAMAMAXXMAXAMASAMXMMMMSSXMAMX
MSASASMMMASAAMMXXXAMAAASXSMSMMMMMXXXAXASMSAXASMSAMMMSXMASMMSMMMAMAMXMSSSSSXAMSXSMASMMSXSAMSMMMAMAMSAMXMSMAAXMSMSSMMSMMMMMMMSAMASXMSXAXMAXSMS
AAAXXMXXSAMXXXMASMXSMMMSASAXXXSXSSMSAXMSAMXMMMXXAASASAMASAXAMSSSSSXMXXAXASAMXXAAMMSAAXAMAMXSAXXMAXXXXAXAASMMAXAMAMASXSAAAAXMAMXMAMXMMSMMXAAA
MMMMASAMMASXMMSMMAASAAXMAMMMMAXAXAAMAMMXMSAMXMXMMMMASAMXSXMMSAAMAMXAMMXMMMSXAMSAMXXMMSASXMAMXSSXSAMXSMSMMMXMSMAMAMMSASXSMSMSMMSSSMXSMSASXMMM
XAXSAMAXSAMMAMAAMSAMAMXMMMMMSAMSMSMSXXXAXSXSAMMXSXMAMXMASAMXMMSMMSXSSSXMAAAMAXMAMAXSASAMMMMSMMXAMXSXAMXMAMXAXSAMASXMXMAXAMAAXXXAXXXMAMAMXXAX
MMMMAMXMMXSSSSSSMMSXAMAAAAAMMASXAMAXMMSSMSMSASASMAMSMAMXXAXAMXXXAXMAAMMXMSSMXXXMMMSXASAMXSAAAMMMMAAMAMXSASMSASXSXMMMMSXMASAMXXMXMSXMAMAMXSSS
AXSASAMXMXMMAMAMXAASMMSSSSSSSMMMSMXMAXAXSMASAMMAXAMASMASMMMSSSMMASMMMMMAAMXMMMXXAXXMXMMXAMXSSMAMXAMXMAXXAXAMXSMMAXAAAXXMXMMXMXMASXMSSSMXAMXX
AMXAMXAMMXMMAMAMSAMXMAAXXAXMMAAAASXSXMMMMMMMXMXMSSSMSXAMAAMXAMXMASXXXASMSMSAAAAMXSMSMMXMXSAMAMXMMMXMMSSMAMXMAMASAMSMSSSMSMMASXMMSAMXMAMSMSSM
MAMSMXSXMASXXXAMAMXMMMSSMMMSASMSSSMSAAMSXSASXSAXMAAXMMSXSMSMAMXSMMMMMMSAAAXXMMMSAXMAAXMAAMMSAMMSAMAMXAAMSMSMXMAMXMAAMAMMAASMSAXASAMMMAMAAAXX
XSAASAAASAMAMXSSMMASMAXXAAAXAMXXXXASMMMAASASAMSXSMSMAAXXMAXMAMXMAAXAAMMMMMMXMAXMMMSMSXSSMMXMXSAAMSSSMSSMAMSAXMXMASXSMASXSMMASXMXSAMASXSMMMSX
AASAMXSMMAXXXAMAMSASMMSSSMSSMSSSMSMSAMXMAMMMAMMXMAMAMXSXMAXSASASXMSSMSAMMASMSSMAAMXMAMAMXXAMSAMXXAAAXMAMAXMAMSASASXAMAXXASMAMAAXSMMMMAMAAXMM
MAMXSMMXMSSSMXSAMMXXAAAXAXXAAAAAAMXMASMXMMASMMSMMAMAXAXASAXMASASAMXAXMAXSASAAASXXMMASXSMMSMSXAMXMMSMMMASMSMMMSAMAMMSMASMSMMASXSXMASAMAMASMSA
XXMAXAXAAMAMAAMXMAMSMASMSMSMMMSMSMXMAMXAXMASXAAAMXSMMMSAMXSMMMMSAMMMMSAMMMXMSMMSMASAMAXSAAXAXAMMMXMAMSAMXAMAAMXMAMAMAXXXAASXSAMXMASXSXSXXAXS
SAMXSSSSXMMMMSSMXMMAMXXAAAXMAXXMAXXMASXMSMAMMXSSMAMXAMXMMASMMSASMMAAMMXXASXXMAAASAMAMAMSSMXSAMXMAASAMMMSSSSMSXXMXSAMXMMSMMMMMXMASMXMAMXMMSMX
SXXXXAXAASXMXMAMAXSXMMMMMXMSXXAXXXMMASAAAMXXXXAAMMXMSMSAMMXSAAMMASMSXMASMSAMSMMMMMSAMAMXAXXXSMAMXXXXXXXXAAXMXXSMAMAMAAAASXXAMMMMSAMSMAAXSAAX
XAMMMMMSMMAMMSAMMMSAMXMMXXMXMASXMMSSMSMMMSMASMSMMSXMMAMXXMAMXMXSAMXMXMASAXMMAAXAXXMASXSXMMMSASXSSSMMSMSMMMMMXAXMAMAXSSMMASXMXSASMMMAMSMXSMSM
MMMSAAAAXSAMAMASXAXAMAMSSSMXAMAAAAAAXMAXMAMXAAXMAXAMMXMSSMMXSMXMASASASAMMMMSXSSMSMSMAMSAMXXSAMXAAAAAAAMAMMAMMMMSAMMXMAMXMAXSASMXAASAXAMAMAAX
AAAMSMXSXSASXSSMMSMMMMSAAAXAMXSSMMSXMXMASXSMMSMSXSSMSXAXAASAMXAXMXMXASMXSAMSAMAAAAAXMASMMMMMAMMMSMMXMSXMMSASAXASMMMASASMXMMMAXXSSMSMXAMMSSSS
SMAXXMMXXSXMASAXAXASAMMMSMMMSAMXXMAMSMSASAMAAMXMAMAAXMXMMAMXSSSSMSSMMMAASASMSSMMMSMSXMSXMSASAMXXMAXAXAASASXSASXMAASMSASMXXXMAMMXMAXMSSXMAAXX
AMMAMXMMASAMXXMMMXMSASAAAXXMAXMMMXMXMAMAMXMMMSMMAMMMMMXSXXSXMAMXAAXAXXMASXMAXXAAXAMXAXMAAMXSMSMAXASXSMMMASAMXMAMSMSAMXMMSSMMXSMAMMMMAMASMSMS
XSMMMMSAAMMSSXMASXXSMMMSXMASMSMASAXAMSMSMSMAAXAXXSXAAMAMAXSMMAMMMMSSMXSAXXMMMSXMXSXSSMSMMSMMAAXXMXSAAXXMXMASAMAMAAXAMXAXMAASAMMXMAXMASXMAXXA
AAAXXAXMMMXAAASASAMXSXXMASASAAXMSAMMSMAAASMMSSSMAXMXXMAMAMMASAMXXMAMXAMMSMSMASMSXMAAAAXMXAAXSMSMMSMXMMMSXMAXMSSSMMSAMSSSSSMMAMAAMXSSMSMMMMMM
SSMMMMSMAXMMSMMASASAMMMSMMMMXMXXMAMSAMSMSMAXMAAMMMSXMSSSXSXMSXSSMMASMMMXAAAMXMASAMMMMMMSSSSMXXXAMAMXMAMMAMXMMAMXAXXAMXAXAAMSSSSXSSMMAMXAAAAX
AXAAAAAXXSMXXMMAMXMASAAAAASMSSSMMAMXAXXMXMXMMSMAXAMXMAAAAMAXSXAAXXAMAAXSMSMSMMAMMMAMAAXXAAXASXSMMAMXMXMSAMMXMASMSMSSMMMMSMMAAMAXXAAXMASMSSSS
MSSMSSSSMAXAAXMASASXMMMSSMSAAAAXMAXMMMMSMSMMXMMSAXSAMMXMXXAAMMSMMMASAMXXAAAAXMASXXAMMSSMMMMMSAASMSMASAAMASMASXMAMXAXXXXAXAMMMMMMMAMMXXXMMXAA
XAXXMAMXAMMMSMXAMMSMMMAAAMMMMSMMSSSSMAAAAAASAMAXAMSASAXSMSMSXAMSSMMMXMXMSMSMXSMSXSSSXAXMAXSAMMMMXAAASMSMMMMAXAMXMMMMMSMMSSMXMAMAAMMMXSASMMSM
MMSMSASMSXAXXXMMSAXAAMXSMMAXXAAMXMAAXMAMSXXMASMMXMXAMAXMAXAAMSAAMMAXAMXAAXAAASXMXAAXMSMSSSMAMMAMSAMXSAMXASMSXSMXMASAAMAMXMASXMMXSAAXXMAMXAMX
XXAAXSAAAASXMXAAAXMMMSXAXSAXMAXMAMMMMSAMMMXMAMXXXMXSSSXMSMAMSMMASXMSMSMSAMMMMMAXMSMMAAAXMAMAMSAMMAMXSXSMMSAMXXXASASMMSAMAMXMAAAAMXMMSMSMMSSM
ASMMMMMSMXMAAAMMSMSMAMMMMMASASASXMASASXAAASXSAMMMAXAAAXSMSXXXAMSAMXAXAXMASXAXSXXAAASXMXMXAMXXXAMSSMMMAXAMMXMAMAMMASAXSMSAXAXXMMXXAMMXAAAXAMA
MMASXMMAMASXSMSXXAXXAXAAXMASMAAMASXSAXMMSMXAMMSAAAMMMMXMASXXMXMXMASASXXSAMXSXSSSXXAMXAMSSMSSSSSMAAAXMAMSXMMMSSMMAAMMMXAXASXSASASXSMSMSMSMSSS
AMAMAASASXSMXAXAMAMMSSSSSMASXMAMXMMMMMAAAMMMMASMSMSAXXMMXMXXMAMXXAXXMAXMASXMAMASXXSASMMAAXAAAAAASXMMMAMXAMSAMAXSXSMXSMSMMMMAAMASAXAXMASXAMAM
MMSSSMMASASAMAMXMAMAMAMAXMXSXXMXMXAAAMMMMXAXMXSAXXSAMAASMMMMMAXXMAXMASASAMXMAMAMMXXAAMMSSMMXMSMMMAAAXSSSXMMASAMSAMMAXAXMXAMMMMMMMMMMSXSMMSMS
SAMXMXMMMAMSMXSXMAXXMAMAXXAMXXSAASXXMMAMXSXSAXMASMMSMSMMAAAXSSSXSMMMAMXMASXSXMXSMAMMMXAAMMSMXMASXXMSSMAMMAMXMASMAMMMMSMSSMMSXXAAAXMASAXAXXAA
MXXMXMMMMXMASMMMXMSXSAMXSSXSAAMMMMSAMSMMXMAXXXXMMAAAMXAMSMMMMXAXXAAMASMSMMMXAMXAMASXSMMXXAAXAMXAMXMXAMAMXSMMMMAMAMAAAAAXAXMAASXXXSMASMSMMMXM
SMXSAAAMSSMSAMAAASAMSASAAAAMMSSXSMMSMAXAMXMSMXSMSSSSXMSMXASMSAXMSSMSASMAAMAMXMXMMMMAXAMAMSSSXSAMAAMMSMAXAMAMXMASMSSSSXSMMMMSXMAMSAMXSMMAAAMX
AMASXSMSAAMAMSMMMMAXXAMMMMMMAXXAMAAAMMMSMSMAAMSAMMAMMAAMSMMAAXMMXAAMASXMSMMSMAASASMMMXMAMXAMASMMXXSAMMSMASAMSSMSAAAXAAXASAMXAMXMAASAMXSSMSSM
MMAXAMXMXMMAMMMSSSXMMSMXMSMMMSXSMMSSSXMAAASMSMMAMSAMMSMMAAMMMSAMXMMMMMXMAAAAMSMSASAMSSSSSMAMASMXSAMMXAAMMMAMAAXSMMXMMXSXXAXSAMXXXMAXXMAXAAXA
XMMSMMASMSSMXSAAXAXMAXAMXXAAASXMAXAMXMSMSMSXMASMMMXMXAXSSSMAXXXAMXAXXAMSSMMXXXXMMMAMSAAAXXAMXMAAMAMXMSMXXSXMSSMMAMMAMAMMSMMXMMMSAAXXXAXMMMSS
MMAAASASXAXSAMMSSMMSAMXMMSSMMSASAMXXMASAAASAMMXXSXMMXXMAMXMXMMMXMSXSMMMMXSMXXMMXXMAMXMMMMSXSSMMMXSMXMMAMMMMMAMASAMSAMASMAMMAXAAXMASMMSSXXXXA
MSSMMMMSMMMMMSAXAAMMMXAXAMMMMSAMXXXXAMMSMMSAMAMXMASXSSMSSSMASASAMMMMXMAMAMXMAMAAMSAMXSXXXXAAXAXXAXAMXMAMXAAMAXXMMXSAXAMXAAMXMMSXMMXAXASMASMS
MAAXXAMSASASXMXSSXMASMSSSSMAMMAMXSSMSXXXMMXAMMAAMAMAAXAAAXMMSAMMMAXAASAMASAXAXMAMAAXAMAXXMSMSXMAMXAMSSSSSMMSSSMASASXMSXSSSMSXAXMSMSSMAMMMMAM
MSSMSMMSAMASAMXMASMXMAAMAAXMSAMXAAAMMSAMXSSMMXSMSMMMMMMMSMSXMMMXSAMSXSMSMSMSMMMXSSXMASMMXXAXXAMAMMMMXAXAMXMXMAMAMMMMAMAMAAAMMSMMAAMXMAXAXMAM
AAAAXXAMXMAXAMXSAMXMSMSMXMASMAMMMSXMMMMSSMAMSAMXMMSAMXAXAAXMASXXAMAMAMXSXMASMASAMXXMAXAAXSMSSXMAMAAAMXMMSMSAMAMSMSXXAMXMSMMMAAASMSMMSSSMMSAS
MMMSMMXSAMSSMSMMSSXXAAAXMXMMSMMAAXMAMAAXASMMSXMXXAXMMSSSMSMMXMAMMASMMMAMAMAMMAMASASMSSMMXSAAXASASMSMSAAXAAASMAMMASAMSSMAMSXMSSMMAMXMXMAXMSAX
SAMXXAASMSXAASXAXMASMSMSMAXXAMMSMMSSSMXSAMXAXAMAMXXSAAAAMXMASXSAXAAAXMASXMXSMAMAMAXXXAXSAMXMXXMAXAAASXSMMSMXMXXMAMAMAAMXMXXXAMMMSMMMMSSMMMSM
SSSMMMMSXMXMMMMMSXAAMAXAMSXMXSAAAAAAXXXMAXMASMMASAAMMSSMMMAMAAMMMXMAMMMSXMXMXMXMMSMMSMMMAMSMSMSSMMMMMMXMAXXAASMMXSMMMSMMMMMXMMMAMAMMAXAAAAAX
XXXAASASASXXXXAXMMMSSMSSXXAXAMMSMMSXSAMXMMSAMXMASMSMMMAMXXAMMXMASXSSMSMSXSAMSMSMAAXMAMXSAMAAAAAXAMASAMXMASMMSMAMXMASMXXXAAXMXMASMSMMSSMSMSSS
MMMSMSASMMMAMSSXSXXAMXXMASAMXXAMXAMAXMASMAMMSXMASXAAAXAMXSXXSASXSAAXAAAMASMSAAAMSMMSASASXSMSMSXSAMXMASAMASASAMAMXXAMAMSSSSMMAMMMAMMMAAXAAXAM
AMXMAMAMXAXAAXMAMXXMMMSMAMASAMSMSASMMXMAMAMMSAMASXSSMSMSAMMMSASAMMMMSMSMAMXSMSMXMMASAMXMASXXXAAMXMXSSMMMSSMMMSSSMMSMSMAAXAMSASXMSMSMSMMMXMSM
XSAMAMMMSMSMSSMSMMSXAAXMAXXMASMASAAAXXAMSXSASAMASXMAXAMXAAXAMXMXMASAMAXMASXMAMXSASASMMSXASMMMSXMAMMMAAXMXSXSXAMAAAAAAMMSMMMMASXAAAXMXASXSMMS
XMASXMAMAMXMAAAAAMXMMMMMXXSSXMMAMXMMMMXMAMXMSMMASXSXMMMSSSMMSASXSASAMXXSASMXMXAMAMXXXMXMXMASAMASXSASMMMMAMXAMXXSMSMSXSSMMASMAMXSMSMMSAMAAAXA
XSAMXSXSAMXMSSMXSMAXAXSXSAMXMSMASXSAXMAMXSMXSAMASMMASAAMAMXXSAMXMXMAMMMMMMMAXMSMXMXSSMMAMSSMAXAMMSASXSAMASXSXSAXAXAMAMAMSASXSAXXXAAAMMMSMMMM
MAXAAXXSXSAAAAMAMMMMXSAASXMAMMXXSASAXSASASAMSAMAMXMAXAMMAMMAMAMASMXMAMAAAASAMAAMMSAMAAASASMSSMXSMMMMMSXSAMXAAMMSSMSMAMAMMASAXMMMSSMMXMAXAMAX
AMMMASAXASMSMSMASAMAXSMMMASXMASMMMMAMXAMASMAMXMXSMMSSSSSSMMAMSMAAAMAMSSMSXSMXSMSAMASMMMMXSAAMAMAAAMAAMMMMSMMMMAMAAXMAMASMAMXMAAMMMAMSMMSMSSS
XXMXMAMMMSAMXAMXMAMSMMAASMMASAMXAAMXMMSMMMXMSSXXMMAAAAAAMASXXMMSSMAXMAAMXXMMAXAMAXAMXAXSXMMMMXASXMSSMXAAAAMXXMAXMMMXXSASMAMSMSXSXSAMAAAXAAXA
SMMMMAXAMMXASXSSSMSMASXMSASAMASMSMXMAAAASMMAAMAMXASMSMMMMXMSAXXAAXSSMMSMXAAMASASXMSMMMMSMMMMSXMXXXXAASMSSMMSXSSSSXSAAMAMXSSMAMAMXSXSXSMMMMSM
AAAAXASMSAMXAAXXAXAXMMSMSAMSMXMAAMSMMMSMMAXMMMMXAMXXMXXXSXASXMASMMAAXAAASMMSMSAMXMAAASASAAAAMXMMMMMMXMAAMXASAMMAMAMMMMMMAMAMAMAMMXAMAMXXAAXX
MSSXSAMXMASMMSMSMMMSMMAXXXXMMAMXMAAAAAAASAMXMASXMSSMXMXMXMAMAMMXXSXMASMXMXAAAMXSASMSMMAMSMMMXAMAAXAMAMMMXXAMAMMAMMMAMASXAMAMSSSMMMAMXMASMMSM
XAAASXMXSAMXXAAAXAXAASMSAMAMMAMXXSSSMXXMMMMSMAMAXAAAAAASASASAMXMASMXAMXAAMSMSMASMSAMMMSMMMMXSASMSSXSASAMXMSSSMMAMAMXXAXSMSMXXXMAXSASXSXSAAAM
AMMMMAXXXAXXXMSMSSSSMMXAAMAXSXSMXAAAAASMSAAMMXXMMXXSSSMSAMXSMSMMAMAASMSMSMXAAMMMMMMMAAAAXAAASMMAAXMSAMASXAXAAXMSSSSSMMXXMAMMMSSXXSASAMAXMMSA
MMMSSMMMSSMMSMXXXMAMAAASXMMMSAAXXMSMMMAASMSMSAAMMSXAAXMMMMAXMAXMMXSSMMAXXXXMMMMAMAAXMSSSSMMMSASMMMMMXSAXXSMMMMMAMXAXASXXXAXAAXMXMMMMAMMMSSMA
AAAXAAAXAAAAAAXSAMAMXAMXXXXAMXMMMXXXXXMMMAAXMMSAASMMMMMASMMSAMXMAMMAMSMSSMMMAAXAMSXSAAAMMASASMMAMXXAMMMMXXMASAMASMMMAMAASXSSSSXXMASMXMXAXAXX
MMMSSXSMMSAXMMMXAMXSSSMMMMMMSASASMMSSMXXMMMSAAMMSMXXAASMSAASAMXMAXXAMXXAAAMSXSSXMAAMMMSMSAMMMXSAMMMXXAXSMSMASASASAXXXMMMMMAXAMXMSAXSASMMSAMM
SAMXXAXAXXXSSSMSSMAMAAAAAAAMSASAMSAAASMSMAAXMASXXMASMXSAMMMSXMSSMSSXMAMMMSMMAMMMAMXXXAXMMAMMMAMMXAAMXMMAAAMMSXMXSXMMXXASMMMMAMAXMASAMXAXXMSA
SMSSMSMMAAMAMAAAXMAMMXMXXMMMMAMAMMMMSAMMXMXSAMXXAMAXMASXSAMMMMAXAAXAMXMSAMAMXMAMXSMSMASMSSMAMMSSSSMSAXXMSMSMSXSAMAMSAMXXAAMSASXMMXMMXSMMAMAX
SAAXAMASXXAAXMMMSSSSSMSSSMMAMMMXMMSMXASAASXMASASMMASMMMAMXAAMXXMMMSSMAAMASXMSMSMXMASMAMMAMSMMAAMAAASAXSAMAXAXAMMXAMXASMSMMXSAMMSSSMSAMMSSMXS
MMMSMMAMAMSMXAMXAAMAMSAAAXSAMMSAXXAASMMXXSAMXMXXAMASAXMXMSMMSMMXSXAXXXMSXMMXAAXMAMSMMSSMAXSXMMMSSMMMAMMAMXMAMSMMMAMMMMAAXSXMSMMAAAAMMMAAAXAM
SSMAAMSMMMAASXSMMSMAMMMMMMMASASXSSMMMMASXXMMMMMSMMXMAMSAMMSAAMMAMMXSXSXSASXSMMMSASMXAMXMSSMMXSAMAASMSMSXMSMMMMASMSMMMMMMMMAAAMMMSMMMSSMSSMMS
XAMMSMAAXSMXAAMMMMMASAXXASXMMASAMXMAMMASMMSAMAAAMMMMSMMAXAMMSAMASMMMASASAMAMAAASMSMMMMAMMAMAAMASMXMAXXAAAXSXAMSMAMSMASXMAXAXMASMAMXAAAMMXMXM
SMMMMMSSMXMXMXSAMXSASXMMXXAAMXMXMAXAXMXXAMSASMSMSAAXAASMMMSAXMSAMXAMXMAMAMMSMMMSAMMASMMMMXMSSSMMMAMSMMSMMAASMMAMAMASASAXSAMXXAXMASMMXMMXAMAS
SAAXMAMAMAMXXMSXSXMASMMMSSMMMAMASXSMSMSMSMMMMMAASMSMMMMXAMXAXXMAMSSSXMXMXXMAMMXSMASASASXSMAXAMXASXMAAAXAXAMMMSMSMSMMMMAMXAXAMMMSAXAXSMXSMSAS
SSMSMMSAMSAMXXMMSAMSMMSAAMMXMAXMSAAAAAAXMAMSAMMMMAXAMASMSMMMMXMAMAAMXMXMXXMAXSAMXXMAMAMAAMXMAMSAMXMSXMMMXXXSAAXAAAXAAMSMSSMSMSMMAXSMSAASXAMS
MAMXAAMXMXMAMMAAMAMXXAMMXMASMMSXMXMMMSMXSAMSXSSXMASMSASAMXAMSSSMSMXMASAMXASAMMAMMAMSMXMSMMMMXMAAMXMAXSAMMMMMSSSMSAMMMSAAXMAMAMXMSMMASMMMMXSM
SXMMMMSXMASMSMMSSXMMMMSSMMMSAASMMASXMAXXMAXMMAXASAMMAMMAMSMMXXAXXXASASMSAAMASXMMSAAAMXXXAAXMASMXMMMAMMAXXAAAMMXXMAXSMMMSMMAMAMSXMAMAMASXMSSX
SMXAMXXXMMSXAAAXMASAAAAXAAXMMMMAXAXAXXMAMXAAXAMXMASAMXSXMSXSASXMAXXSAMASXXSAMMAAMASMSSMSSMXSASXXSAMXMSSMSMSSSSSSMSMSAAAMXMASAMSAMAMASAMAMAXM
SSSSSSMMSAMMSSMXSAMMMMSSSMSXMMSMMMMMMSXMAMMXMMSXSXMASAAASXAAAMMMSMMMAMAMAMMMXSMMSMXXXAAXMXAMXSAMSAMXMAMXAXAAXXAXAMAMSMMMASASXXSAMAXASXMXMAXA
MAMAAAAAMAMMMAAAMAXXXAXAXXAAAAAAAAASAMASAMSASXAAMMAMMMMXMMXMSMXAMASMXMASXMASAMAMXMAASMSMSMXSAMAMXAMXMSSSMSMSMMMMMMAMXXXSASAMMMXAMASMMMXSAXSS
MAMMSMMMXSMSMXMXSAMSAMMSMSMMMSSSMSMSASMMAMSASAMXMAXMAMSASMSAAMMMSAMXAXASMSASXSAMSXSMSXMASXMMXSXMXSAMXAXAXXMAAAAAAMASMAAMXMAXAMSMMXSAAMAAXMAX
SXSXXXMXMXASASMXMMXSAMXAAXASAMXXXMASAMXMXMMXMXXAXSMSAMSXMAMXASMASASMSMMSAMASASASMAXAXMMAMAMAMMMMAMSAMXSXMMAMSMSSMSASMAMAMMSMMXAAAASXMMMXXXXX
AAXMXMAAXMAMAMSAMXXMXMSMSMMMAXXSAMAMASXSSSSMSMXMSMAXAMXAMXMXMXMAXMMAXMAMMSMSAMMAMMMSMAMAMAMAMAAMASXSMMAMXXMXXAAAXMMSASXSASMAXSMSMMSXMASMMSSS
MSMSAMSSSMXMXMSMMMMSMMAAAAXMMMMAMMAXMMAXXAAAXAASAMMSMMSXMMMAXAMMSMMXMMMSMSASMXSAMXAAXMSXMSSMMSSSXSAXMAMSASXSMMMSMXAMAAAASAMSMSAAMAMASXSAAAXS
XMAMXMAXAMXXXASXMAMAAXMSSMMXAAXXMSMXSMXMMSMMMSXSAXXAAAXAXAMSSMSXAAAASASAAMAMMMSASXSMMXMMMXAAAXAXXMMMMSMXAMAMXSAXXMASXMMMXMAXASMSMASMMASMMMMX
SMSMMMSSMMSSMMMXSSSSSMMAXASMSSSMMASASMXAAAMXAXMMMMSSSSXSMSSMAMMMMXSAXMMMSMAMAAMAMAAXAAAXMAMMMSASXMMAXAAMSMSMAMXXAXAAMASAMXAMXMAXMMXAMAMXXMAM
AAAMSAMAMAXXXAMXAAAAMXMSSMMAAAAASASXMASXSSSSMMMSAMXAAAAMMMAMMMSSXMMMSMSAMXASMXSAMSMMSMSMMXSAXMAMAASMSMSMMAXMMSASXMXMSAMASMASMMMMAMSAMASMSMSA
MSMSMASAMXSXSXSMMMMMMAAMAMXMMMSMMMSAMAMMAMAAXASAAXMMMMMMASAMXXAXSXAXAAAAMSXSAASAMXAAXSMXAASMSMAMXMXAAAAAMAMAXMASMAAXMASAMMAXMAXSAMSXMASMAAMM
XXMXMXMASAAMAMXMXXMASXSSSMAXAXXMMMSMMASXMMSMMSSSXMASXMASXMASAMXSMSAMAXSAMXMMMMSSMSMMSMXMMMSSSXXSXXMSMSMSMAMAMAMXASMXSAMMSMXSMAMMAXMSAMXMMMMX'''

example_input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''


from functools import reduce

def load_puzzle(input):
    lines = input.split('\n')
    puzzle = []
    y = 0
    for line in lines:
        row = []
        x = 0
        for s in line:
            row.append(s)
            x += 1

        puzzle.append(row)
        y += 1

    return puzzle


def find_starting_candidates(puzzle, s, length):
    matches = find_matching_cells(puzzle, s)

    candidates = dict()
    distance = length - 1
    for candidate in matches:
        x = candidate[0]
        y = candidate[1]
        possible_directions = [1,1,1,1,1,1,1,1]  # could optimise with bitflags
        if y - distance < 0:
            possible_directions[7] = 0
            possible_directions[0] = 0
            possible_directions[1] = 0

        if x + distance >= len(puzzle[0]):
            possible_directions[1] = 0
            possible_directions[2] = 0
            possible_directions[3] = 0
        
        if y + distance >= len(puzzle):
            possible_directions[3] = 0
            possible_directions[4] = 0
            possible_directions[5] = 0
        
        if x - distance < 0:
            possible_directions[5] = 0
            possible_directions[6] = 0
            possible_directions[7] = 0

        candidates[(x, y)] = possible_directions

    return candidates

def find_matching_cells(puzzle, s):
    matches = []
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == s:
                matches.append((x, y))
    return matches


def remove_margin_cells(puzzle, cells, margin):
    filtered_cells = []
    for cell in cells:
        if not is_in_margin(puzzle, cell, margin):
            filtered_cells.append(cell)
    
    return filtered_cells


def is_in_margin(puzzle, cell, margin):
    x = cell[0]
    y = cell[1]
    if x - margin < 0:
        return True
    
    if y - margin < 0:
        return True
    
    if x + margin >= len(puzzle[0]):
        return True
    
    if y + margin >= len(puzzle):
        return True
    
    return False


def filter_non_x_mas_es(puzzle, centers):
    filtered = []
    for center_A in centers:
        if has_nw_se_mas(puzzle, center_A) and has_ne_sw_mas(puzzle, center_A):
            filtered.append(center_A)

    return filtered


def has_nw_se_mas(puzzle, center_A):
    return has_nw_mas(puzzle, center_A) or has_se_mas(puzzle, center_A)


def has_ne_sw_mas(puzzle, center_A):
    return has_ne_mas(puzzle, center_A) or has_sw_mas(puzzle, center_A)


def has_nw_mas(puzzle, center_A):
    return has_mas(puzzle, center_A, 7)


def has_se_mas(puzzle, center_A):
    return has_mas(puzzle, center_A, 3)


def has_ne_mas(puzzle, center_A):
    return has_mas(puzzle, center_A, 1)


def has_sw_mas(puzzle, center_A):
    return has_mas(puzzle, center_A, 5)


def has_mas(puzzle, center_A, direction):
    if not has_neighbour(puzzle, center_A, direction, 1, 'M'):
        return False
    
    opposite = (direction + 4) % 8
    if not has_neighbour(puzzle, center_A, opposite, 1, 'S'):
        return False
    
    return True


def update_candidates(puzzle, candidates, s, distance):
    inactive_candidates = []
    for candidate in candidates.keys():
        directions = candidates[candidate]

        active = False
        for d in range(8):
            if directions[d] != 0:
                if has_neighbour(puzzle, candidate, d, distance, s):
                    active = True
                else:
                    directions[d] = 0

        if not active:
            inactive_candidates.append(candidate)

    for inactive in inactive_candidates:
        del candidates[inactive]
    
    return candidates


def has_neighbour(puzzle, position, direction, distance, s):
    x0 = position[0]
    y0 = position[1]
    if direction == 0:
        x = x0
        y = y0 - distance
    elif direction == 1:
        x = x0 + distance
        y = y0 - distance
    elif direction == 2:
        x = x0 + distance
        y = y0
    elif direction == 3:
        x = x0 + distance
        y = y0 + distance
    elif direction == 4:
        x = x0
        y = y0 + distance
    elif direction == 5:
        x = x0 - distance
        y = y0 + distance
    elif direction == 6:
        x = x0 - distance
        y = y0
    elif direction == 7:
        x = x0 - distance
        y = y0 - distance
    
    return puzzle[y][x] == s



puzzle = load_puzzle(input)

# # TASK 1
# candidates = find_starting_candidates(puzzle, 'X', 4)
# candidates = update_candidates(puzzle, candidates, 'M', 1)
# candidates = update_candidates(puzzle, candidates, 'A', 2)
# candidates = update_candidates(puzzle, candidates, 'S', 3)

# count = 0
# for k in candidates.keys():
#     count += reduce(lambda i, j: i + j, candidates[k], 0)

# print(count)

# task 1 answer is 18 for example_input

# TASK 2

centers = find_matching_cells(puzzle, 'A')
centers = remove_margin_cells(puzzle, centers, 1)

x_mas_centers = filter_non_x_mas_es(puzzle, centers)
print(len(x_mas_centers))

# task 2 answer is 9 for example_input