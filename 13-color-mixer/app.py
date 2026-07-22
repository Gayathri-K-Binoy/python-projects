print("COLOR MIXER")
color_mixes={
    ("red","white"):"pink",
    ("red","blue"):"purple",
    ("red","yellow"):"orange",
    ("yellow","blue"):"green",
    ("blue","green"):"teal",
    ("red","green"):"brown"
}

while True:
    color1=input("\nEnter first color: ").lower().strip()
    color2=input("Enter second color: ").lower().strip() # "red    " => "red"

    mix= None#when you want to assign non-value/null
    if (color1,color2) in color_mixes:
        mix=color_mixes[(color1,color2)]
    elif (color2,color1) in color_mixes:
        mix=color_mixes[(color2,color1)]
    if mix:
        print(f"When you mix {color1} and {color2}, you get {mix}!")
    else:
        print("I dont know what those colors make when mixed.")
    if not input("\nMix more colors? (y/n): ").lower().startswith("y"):
        print("Bye!")
        break 