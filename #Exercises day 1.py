#Exercises day 1
#%%
def greet(name):
    print("Hello, " + name + "!")

greet("World")

#%%
def goldilocks(bl):
    bl_min = 140
    bl_max = 150

    if bl<bl_min:
        print("Too short!")
    elif bl>bl_max:
        print("Too large!")
    else:
        print("Just right. :)")
    return


goldilocks(200)

#%%
def squarelist(x_list):
    return [x**2 for x in x_list]

print(squarelist([1,2,3,4,5]))


# %%
def fibonacci_stop(fib_stop):
    fib_list = [1, 2]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib >= fib_stop:
            break
        fib_list.append(next_fib)
    return fib_list

print(fibonacci_stop(100))

# %%
def clean_pitch(meas_pitch, stat_sig):
    for i in range(len(meas_pitch)):
        if stat_sig[i] == 1:
            meas_pitch[i] = -999
    return meas_pitch

meas_pitch = [-1, 2, 6, 95]
stat_sig = [1, 0, 0, 0]

print(clean_pitch(meas_pitch, stat_sig))
# %%
