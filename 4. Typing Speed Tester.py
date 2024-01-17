import tkinter as tk
import random
import ttkbootstrap as ttk


class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        master.title("The Typing Speed Test")
        master.geometry('800x600')
        master.config(padx=20, pady=20)

        # Initialize counts as instance attributes
        self.correct_count = 0
        self.incorrect_count = 0

        self.heading_text = ttk.Label(text="To start the test use the button below", font="Calibri 24 bold")
        self.heading_text.pack()

        self.instruction_label = ttk.Label(
            text="\n\nOnce the test starts words will appear on screen 📺\n\n"
                 "Once you have typed the word and pressed space or enter the next word will highlight.\n\n"
                 "The test will last 1 minute ⏰, and at the end your scores will be displayed.\n\n"
                 "We'd advise taking 2 minutes to rest between tests 😴",
            font="Arial 16"
        )
        self.instruction_label.pack()

        # BUTTON CLASS - initialise
        self.start_button = ttk.Button(text="Click to Start Test", command=self.test_started)
        self.start_button.pack(pady=50)

        self.tkinter_time_left = tk.IntVar()
        self.timer_label = ttk.Label(master=self.master, text='1 minute left', textvariable=self.tkinter_time_left)

        # Display random words during the test (placeholder)
        self.word_chosen = tk.StringVar()
        self.word_label = ttk.Label(master=self.master,
                                    text='Word',
                                    textvariable=self.word_chosen,
                                    font="Calibri 24 bold")

        # User input field
        self.user_input = ttk.Entry(master=self.master, font="Calibri 18")

        # Score label
        self.score_label = ttk.Label(master=self.master, text="Score: Correct: 0, Incorrect: 0", font="Arial 16")

    def pick_a_word(self):
        chosen_word = random.choice(random_word_list)
        self.word_chosen.set(chosen_word)

    def test_started(self):
        self.heading_text.config(text="Test Started - good luck")

        self.instruction_label.pack_forget()
        self.start_button.pack_forget()
        self.timer_start(60)
        self.timer_label.pack(pady=50)
        self.pick_a_word()
        self.word_label.pack(pady=50)
        self.user_input.focus_set()
        self.user_input.pack(pady=50)
        self.score_label.pack(pady=50)

        # Bind the space key to a function for checking input
        self.master.bind('<space>', self.check_input)
        # Do the same for enter
        self.master.bind('<Return>', self.check_input)

    def check_input(self, event):
        typed_word = self.user_input.get().strip()
        correct_word = self.word_chosen.get()

        if typed_word == correct_word:
            print("Correct!")
            self.correct_count += 1
        else:
            print("Incorrect!")
            self.incorrect_count += 1

        self.pick_a_word()
        self.user_input.delete(0, tk.END)
        self.update_score_display()

    def update_timer(self, time_left):
        if time_left > 0:
            self.tkinter_time_left.set(time_left)
            self.master.after(1000, self.update_timer, time_left - 1)
        else:
            self.tkinter_time_left.set(0)
            self.game_over()

    def timer_start(self, start_val):
        self.tkinter_time_left.set(start_val)
        self.update_timer(start_val)

    def update_score_display(self):
        self.score_label.config(text=f"Score: Correct: {self.correct_count}, Incorrect: {self.incorrect_count}")

    def game_over(self):
        self.heading_text.config(text="Test Finished - well done!")
        self.instruction_label.pack_forget()
        self.start_button.pack_forget()
        self.timer_label.pack_forget()
        self.word_label.pack_forget()
        self.user_input.pack_forget()
        # Restart button
        self.restart_button = ttk.Button(text="Click to Try again", command=self.reset_test)
        self.restart_button.pack(pady=50)
        # Unbind key events
        self.master.unbind('<space>')
        self.master.unbind('<Return>')

    def reset_test(self):
        # Reset counts
        self.correct_count = 0
        self.incorrect_count = 0

        # Reset labels and widgets
        self.heading_text.config(text="To start the test use the button below")
        self.instruction_label.pack()
        self.start_button.pack(pady=50)
        self.timer_label.pack_forget()
        self.word_label.pack_forget()
        self.user_input.pack_forget()
        self.score_label.pack_forget()
        self.restart_button.pack_forget()
        self.update_score_display()
        self.user_input.delete(0, tk.END)


if __name__ == "__main__":
    random_word_list = [
        'little', 'brother', 'dull', 'gifted', 'sniff', 'used', 'round', 'breath', 'deserted', 'disagree',
        'parcel', 'grouchy', 'vague', 'insidious', 'weather', 'dress', 'frightened', 'comfortable',
        'dinosaurs', 'glistening', 'society', 'turn', 'sea', 'corn', 'aware', 'addicted', 'price',
        'awful', 'belief', 'fry', 'hobbits', 'abandon', 'ability', 'absence', 'absolute', 'absorb',
        'abstract', 'abundant', 'academy', 'accent', 'account', 'accuracy', 'accuse', 'achieve', 'acidic',
        'acoustic', 'activate', 'adapt', 'adequate', 'adjust', 'admit', 'adventure', 'aerial', 'affection',
        'affirm', 'against', 'ageless', 'agile', 'agree', 'alchemy', 'alert', 'algebra', 'alien', 'allege',
        'allocate', 'alpha', 'amazing', 'ambition', 'amplify', 'the', 'and', 'you', 'is', 'he', 'she', 'it',
        'we', 'they', 'are', 'was', 'were', 'have', 'has', 'do', 'does', 'can', 'could', 'will', 'would',
        'should', 'not', 'for', 'with', 'by', 'on', 'at', 'in', 'to', 'from', 'into', 'up', 'down', 'over',
        'under', 'through', 'between', 'before', 'after', 'about', 'around', 'along', 'against', 'off', 'of',
        'about', 'toward', 'among', 'within', 'throughout', 'because', 'since', 'although', 'before', 'after',
        'when', 'while', 'if', 'unless', 'until', 'even', 'though', 'as', 'like', 'such', 'because', 'so',
        'though', 'although', 'however', 'nevertheless', 'consequently', 'furthermore', 'meanwhile', 'similarly',
        'therefore', 'moreover', 'otherwise', 'instead', 'subsequently', 'likewise', 'nevertheless', 'nonetheless',
        'hence', 'forthwith', 'thus', 'hitherto', 'whereas', 'otherwise', 'regardless', 'nevertheless', 'whenever',
        'wherever', 'whatever', 'whoever', 'whichever', 'however', 'itself', 'myself', 'yourself', 'ourselves',
        'yourselves', 'themselves', 'your', 'my', 'our', 'his', 'her', 'its', 'their', 'mine', 'yours', 'ours',
        'hers', 'theirs', 'some', 'many', 'few', 'most', 'several', 'all', 'every', 'each', 'other', 'another',
        'any', 'somebody', 'everyone', 'anyone', 'something', 'everything', 'nothing', 'anything', 'nothing',
        'now', 'then', 'today', 'tonight', 'tomorrow', 'yesterday', 'soon', 'later', 'nowadays', 'already', 'yet',
        'still', 'just', 'ever', 'never', 'always', 'sometimes', 'often', 'rarely', 'seldom', 'usually', 'quickly',
        'slowly', 'immediately', 'eventually', 'recently', 'suddenly', 'occasionally', 'finally', 'certainly',
        'definitely', 'probably', 'possibly', 'perhaps', 'maybe', 'likely', 'unlikely', 'analyze', 'ancient', 'angelic',
        'animated', 'announce', 'anonymous', 'answer', 'anticipate', 'anxiety', 'apart', 'appeal', 'appetite',
        'applaud', 'appliance', 'appoint', 'approve', 'aquatic', 'ardent', 'arise', 'aroma', 'ascend', 'asleep',
        'assert', 'astonish', 'athlete', 'atmosphere', 'attain', 'attempt', 'attractive', 'audacious', 'augment',
        'auspicious', 'authentic', 'authorize', 'automatic', 'avalanche', 'avenue', 'awesome', 'awful', 'awkward',
        'balance', 'barrier', 'beacon', 'beautiful', 'believe', 'benevolent', 'bewilder', 'blossom', 'boundary',
        'bountiful', 'bravery', 'brevity', 'brighten', 'brilliant', 'broaden', 'buoyant', 'calculate'
    ]

    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
