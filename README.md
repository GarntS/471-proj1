# CMSC471 Project 1
### Minimax-ab and Chess

### Description:
It is your job to experiment with and report about the strengths and weaknesses
of different evaluation functions and search depths for use with minimax-ab.
You'll write your own evaluation functions and choose your own search depths
while collecting data, and summarize your findings.

### Files:
- `README.py`
	- this readme file
- `baby_driver.py`
	- the driver file containing the main method and some pre-written code to
actually run minimax-ab in the context of chess.
- `eval_func.py`
	- a file containing your definitions of different evaluation functions that
can be used by the minimax to evaluate board positions.

### Instructions:
1. Clone this repository to your dev machine.
2. Using `pip`, a package manager for Python that should have come preinstalled
when you installed Python, install the `python-chess` package. This can be
accomplished by running the command `pip3 install --user python-chess`.
3. Open and skim through `baby_driver.py` and `eval_func.py`. You don't need to
understand all of their inner workings, but reading through the comments may
help you to understand what to do down the line.
4. Within `eval_func.py`, define another evaluation function using the same
format as the provided examples. The `python-chess` package has been imported for
you already, but if you want to use anything else you're welcome to.
5. At the top of `baby_driver.py`, make sure to import any functions you created
within `eval_func.py` so that you can use them.
6. In the `main()` function in `baby_driver.py`, use a combination of evaluation
functions and search depths to collect data on the effects they have on the
winrates of the AI. Feel free to completely grenade the example code that's
there and replace it with some python code that helps you to get that data in a
format that's easy to process, like JSON, XML, or CSV.
7. Anywhere that it's *necessary* that you add code is marked with a
`TODO(y'all):`. If you search your code for that you can easily find all of
those locations, and many text editors will highlight it by default.

### Helpful Documentation:
The documentation for the `python-chess` library can be found
[here](https://python-chess.readthedocs.io/en/v0.30.1/index.html) and is
extremely helpful to figuring out how to use the library. I *strongly* recommend
that you use this to help you.
