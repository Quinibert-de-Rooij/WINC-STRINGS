# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = "Ruud Gullit" #Na wat advies gewoon maar even de oeffening simpel houden.
goal_0 = 32
scorer_1 = "Marco van Basten"
goal_1 = 54
scorers=(scorer_0+" "+str(goal_0)+", "+scorer_1+" "+str(goal_1))
report=(f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute")
player="Hans van Breukelen" #Perhaps not a typical goal scorer, but his name will be chanted when he stops the ball
splt_Name1 = (player.split(' ', maxsplit=1))
first_name = splt_Name1[0]
last_name = splt_Name1[1]
last_name_len=len(last_name)
#last_name_actual_len=(len(last_name)-(last_name.count(' ')))
first_letter = (first_name[0]+ '. ')
name_short=(first_letter+last_name)
firt_name_len=(len(first_name))
chant=(((first_name+"! ")*firt_name_len).rstrip(' '))
good_chant=chant.endswith('!')
"""
Andere probeersels
splt_Name1 = (scorer_0.split(' ', maxsplit=1))
splt_Name2 = (scorer_1.split(' ',maxsplit=1))
frst_Name1 = splt_Name1[0]
frst_Name2 = splt_Name2[0]
first_letter1 = (frst_Name1[0]+ '. ')
first_letter2 = (frst_Name2[0]+ '. ')
last_name1 = splt_Name1[1]
last_name2 = splt_Name2[1]
print (first_letter1 + last_name1)
print (first_letter2 + last_name2)
int_name1 = len(frst_Name1)
int_name2 = len(frst_Name2)
print(str(goal_0)+"' "+((frst_Name1+"! ")*int_name1))
print(str(goal_1)+"' "+((frst_Name2+"! ")*int_name2))
"""
