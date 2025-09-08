def show_magicians(magicians,new_list):
    for magician in magicians:
        print(magician)
    print("\n")
    for magician in new_list:
        print(magician)

def make_great(magicians):
    new_list = []
    for magician in magicians:
        new_list.append(magician.title() + " The great.")
    return new_list

magicians = ['merlin','gandalf','voldemort']
new_list = make_great(magicians[:])
show_magicians(magicians,new_list)