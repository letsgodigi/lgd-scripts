learnset_lines = []
learnset_lines.append("/* eslint-disable max-len */\n\n")
learnset_lines.append("export const Learnsets: {[k: string]: ModdedLearnsetData} = {\n")
sets_file = open("digimon-sets.ts", "r")
for n in sets_file:
    # Species name
    if '"species": ' in n:
        digi_name = n.split(":")[1]
        digi_name = digi_name.replace(',', '')
        digi_name = digi_name.replace('"', '')
        digi_name = digi_name.replace('\n', '')
        digi_name = digi_name.replace(' ', '')
        digi_name = digi_name.lower()
        digi_name = "\t" + digi_name + ": {\n"
        learnset_lines.append(digi_name)
    # Moveset
    elif '"moves": ' in n:
        digi_moves = n.split(":")[1]
        digi_moves = digi_moves.replace('"', '')
        digi_moves = digi_moves.replace('[', '')
        digi_moves = digi_moves.replace('],', '')
        digi_moves = digi_moves.replace('\n', '')
        digi_moves = digi_moves.replace(' ', '')
        digi_moves = digi_moves.replace('-', '')
        digi_moves = digi_moves.lower()
        digi_moves = digi_moves.split(',')
        # Remove duplicates
        res = []
        [res.append(x) for x in digi_moves if x not in res]
        digi_moves = res
        #
        learnset_lines.append("\t\tlearnset: {\n")
        for move in digi_moves:
            learnset_lines.append("\t\t\t" + move + ': ["7M"],\n')
        learnset_lines.append("\t\t},\n\t},\n")
learnset_lines.append("};\n")
sets_file.close()
learnset_file = open("learnsets.ts", "w")
learnset_file.writelines(learnset_lines)
learnset_file.close()