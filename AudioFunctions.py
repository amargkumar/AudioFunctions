
# Name: Amar Kumar

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  


# Function to write #1:  scale

def scale(L, scale_factor):
    """scale accepts a list and
       returns a list of elements each of which is scale_factor times as large.
    """
    LC = [scale_factor * x for x in L]
    return LC



# Function to write #2:  add_2
def add_2(L, M):
    """add_2 accepts two lists and returns a single list that is an element-by-element sum of the 
       two arguments. If the arguments are different lengths, add_2 returns a list that is as long 
       as the shorter of the two. 
    """
    N = min(len(L), len(M))  # N is the min length!
    LC = [L[i] + M[i] for i in range(N)]
    return LC


# Function to write #3:  add_3
def add_3(L, M, P):
    """add_3 accepts three lists and returns a single list that is an element-by-element sum of the 
       three arguments. If the arguments are different lengths, add_3 returns a list that is as long 
       as the shortest of the three. 
    """
    N = min(len(L), len(M), len(P))  # N is the min length!
    LC = [L[i] + M[i] + P[i] for i in range(N)]
    return LC

# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """add_scale_2 accepts two lists L and M and two floating-point numbers L_scale and M_scale. 
       These stand for scale for L and scale for M, respectively.
       add_scale_2 returns a single list that is an element-by-element sum of the two argument lists, 
       each scaled (multiplied) by its respective floating-point value. If the argument lists are 
       different lengths, add_scale_2 returns a list that is as long as the shorter of the two.
    """
    N = min(len(L), len(M))  # N is the min length!
    LC = [(L_scale * L[i]) + (M_scale * M[i]) for i in range(N)]
    return LC


# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


# Function to write #5:  replace_some

def replace_some(L, chance_of_replacing):
    """replace_some accepts a list L and a floating-point value chance_of_replacing.
       replace_some independently replace—or not replace—each element in L, 
       using the helper function randomize.
    """
    N = len(L)
    LC = [randomize(L[i], chance_of_replacing) for i in range(N)]
    return LC


assert replace_some(range(40, 50), 0) == list(range(40, 50))
assert replace_some([42], 1.0) != [42]




# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

# Sound function to write #1:  reverse

def reverse(filename):
    """reverse accepts a filename as did flipflop. The sampling rate does not change, 
       the function creates a reversed set of sound samples, writes them to the file out.wav 
       and then plays that file.
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    newsamps = samps[::-1]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #2:  volume

def volume(filename, scale_factor):
    """volume accepts a filename and a floating-point value scale_factor. 
       volume then plays the sound being scaled in amplitude (volume) 
       by the scaling factor scale_factor.
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    newsamps = scale(samps, scale_factor)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #3:  static

def static(filename, probability_of_static):
    """static accepts a filename and a floating-point value probability_of_static, 
       between 0 and 1. The output samples are replaced with a probability of probability_of_static. 
       When they're replaced, the samples will be random values, 
       uniformly chosen in the valid range from -32768 to 32767.
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    newsamps = replace_some(samps, probability_of_static)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #4:  overlay

def overlay(filename1, filename2):
    """overlay accepts two filenames, and creates a new sound that overlays (combines) the two. 
       The result is as long as the shorter of the two. 
    """
    print("Playing the original sound from the first file")
    play(filename1)

    print("Playing the original sound from the second file")
    play(filename2)

    samps1, sr1 = readwav(filename1)   # get samps and sr from the file!
    samps2, sr2 = readwav(filename2)   # get samps and sr from the file!

    newsamps = add_scale_2(samps1, samps2, 1, 5)
    newsr = max(sr1, sr2)              # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #5:  echo

def echo(filename, time_delay):
    """echo accepts a filename and a floating-point value time_delay, 
       which represents a number of seconds. The original sound is overlaid by a copy of itself 
       shifted later in time by time_delay.
    """
    print("Playing the original sound...")
    play(filename)

    samps1, sr = readwav(filename)   # get samps and sr from the file!

    samps2 = [0]*int(time_delay*sr) + samps1

    newsamps = add_scale_2(samps1, samps2, 1, 1)
    newsr = sr

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

# Helper function - add_scale_3

def add_scale_3(L, M, P, L_scale, M_scale, P_scale):
    """add_scale_3 accepts three lists L, M, P and three floating-point numbers 
       L_scale, M_scale, P_scale. add_scale_3 returns a single list that is an element-by-element 
       sum of the three argument lists, each scaled (multiplied) by its respective floating-point value. 
       If the argument lists are different lengths, add_scale_3 returns a list 
       that is as long as the shortest of the three.
    """
    N = min(len(L), len(M), len(P))  # N is the min length!

    LC = [(L_scale * L[i]) + (M_scale * M[i]) + (P_scale * P[i]) for i in range(N)]
    return LC


# Sound function to write #6:  chord

def chord(f1, f2, f3, time_in_seconds):
    """chord accepts three floating-point frequencies f1, f2, and f3, 
       along with a floating-point time_in_seconds. 
       chord createa and playa a three-note chord from those frequencies.
    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds)
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds)
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds)

    newsamps = add_scale_3(samps1, samps2, samps3, 0.33, 0.33, 0.33)
    newsr = max(sr1, sr2, sr3)

    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    return play('out.wav')

