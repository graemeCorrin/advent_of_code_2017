import argparse
from advent.day.day_1 import Day1
from advent.day.day_2 import Day2
from advent.day.day_3 import Day3


def __run():
    days = __get_input_parameters()
    run_days(days)


def __get_input_parameters():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-d', '--days', type=int, nargs='+', help='days to run')

    args = parser.parse_args()

    return args.days


def run_days(days=None):
    all_days = not days

    if all_days or 1 in days:
        __run_day1()

    if all_days or 2 in days:
        __run_day2()

    if all_days or 3 in days:
        __run_day3()


def __run_day1():
    string = '522883333635584854991545936673798259831295958381745562154597678479248946819836599823272273487661233235' \
             '237619281355294981427594757577433952981197664436151779558699831924224161481362273425579756957157769923' \
             '859266728742816639822157288586941641968268775974397843457182126714651433839462452564833873992947991236' \
             '817266988557731971838927816876684448794876169743872255685788243322439372313129887625262664351723688399' \
             '911566565693552167577286651618589931713249471672361549347639711562768788766519478174637734146899595455' \
             '451825291685922739769388525432962881235561248759444552239585355173456749883838224861613796963797136961' \
             '544359997358832638879289396992485531643795231349255167154571426278473834351716654419719454717351515592' \
             '724417544729647428215411495118164831787582752581445375884619454887278994337228195299522277917381244418' \
             '649111542647618867225324974447894686331791513683219913286891789124359119571935472112911622916468825685' \
             '362833923391967146878191316741562421415279386458533294446842884917187687343362152424228948813567531354' \
             '449824549863742413915378292572374524972874388549387779264857667319688994956831723412586336918795378861' \
             '184138835399987551917289632952434652726523176786883969669332827338177272678294916611293295435692375748' \
             '513936729869992298492597772497294427799168682321929593973431387483486179617959165917472643235753311389' \
             '621278156665915493941986679748834744855171948163257223163246357559159969638822334421922832513423323853' \
             '885428943775633184888724242338754221469115722672517968363896741567869762513817763344476512622388547834' \
             '895133263439829161213485285868394246617832992265582222542653435919169617763316796283984798582667695541' \
             '742661712628825536612316917467434841793215829133464676763776432322684277152359856242939993578978821595' \
             '836736246765244485412395197211835841762967945497868733713767549529576845171963199939861782828767193758' \
             '499869795942584588314573632381822512931184599721498766343337568962174666562918725251164396931528331626' \
             '9222835744532431378945137649959158495714472963839397214332815241141327714672141875129895'

    # Part 1
    result = Day1.captcha(string, 1)
    print(result)

    # Part 2
    result = Day1.captcha(string, int(len(string) / 2))
    print(result)


def __run_day2():
    table = [[1208, 412, 743, 57, 1097, 53, 71, 1029, 719, 133, 258, 69, 1104, 373, 367, 365],
             [4011, 4316, 1755, 4992, 228, 240, 3333, 208, 247, 3319, 4555, 717, 1483, 4608, 1387, 3542],
             [675, 134, 106, 115, 204, 437, 1035, 1142, 195, 1115, 569, 140, 1133, 190, 701, 1016],
             [4455, 2184, 5109, 221, 3794, 246, 5214, 4572, 3571, 3395, 2054, 5050, 216, 878, 237, 3880],
             [4185, 5959, 292, 2293, 118, 5603, 2167, 5436, 3079, 167, 243, 256, 5382, 207, 5258, 4234],
             [94, 402, 126, 1293, 801, 1604, 1481, 1292, 1428, 1051, 345, 1510, 1417, 684, 133, 119],
             [120, 1921, 115, 3188, 82, 334, 366, 3467, 103, 863, 3060, 2123, 3429, 1974, 557, 3090],
             [53, 446, 994, 71, 872, 898, 89, 982, 957, 789, 1040, 100, 133, 82, 84, 791],
             [2297, 733, 575, 2896, 1470, 169, 2925, 1901, 195, 2757, 1627, 1216, 148, 3037, 392, 221],
             [1343, 483, 67, 1655, 57, 71, 1562, 447, 58, 1561, 889, 1741, 1338, 88, 1363, 560],
             [2387, 3991, 3394, 6300, 2281, 6976, 234, 204, 6244, 854, 1564, 210, 195, 7007, 3773, 3623],
             [1523, 77, 1236, 1277, 112, 171, 70, 1198, 86, 1664, 1767, 75, 315, 143, 1450, 1610],
             [168, 2683, 1480, 200, 1666, 1999, 3418, 2177, 156, 430, 2959, 3264, 2989, 136, 110, 3526],
             [8702, 6973, 203, 4401, 8135, 7752, 1704, 8890, 182, 9315, 255, 229, 6539, 647, 6431, 6178],
             [2290, 157, 2759, 3771, 4112, 2063, 153, 3538, 3740, 130, 3474, 1013, 180, 2164, 170, 189],
             [525, 1263, 146, 954, 188, 232, 1019, 918, 268, 172, 1196, 1091, 1128, 234, 650, 420]]

    # Part 1
    result = Day2.checksum_difference(table)
    print(result)

    # Part 2
    result = Day2.checksum_quotient(table)
    print(result)


def __run_day3():
    input_value = 361527

    # Part 1
    result = Day3.steps_to_center(input_value)
    print(result)

    # Part 2
    result = Day3.first_larger_value(input_value)
    print(result)


def __run_day4():
    pass


def __run_day5():
    pass


def __run_day6():
    pass


def __run_day7():
    pass


def __run_day8():
    pass


def __run_day9():
    pass


def __run_day10():
    pass


def __run_day11():
    pass


def __run_day12():
    pass


def __run_day13():
    pass


def __run_day14():
    pass


if __name__ == "__main__":
    __run()