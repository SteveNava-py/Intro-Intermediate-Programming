class Gadgets:
    def __init__(self, explosive_gel, smoke_pellet, disruptor, remote_controller_batarang):
        self.explosive_gel = explosive_gel
        self.smoke_pellet = smoke_pellet
        self.disruptor = disruptor
        self.remote_controller_batarang = remote_controller_batarang

    def display_info(self):
        print("Gadget Information:")
        print(f"Explosive Gel: {self.explosive_gel} - Used for controlled explosions.")
        print(f"Smoke Pellet: {self.smoke_pellet} - Creates a smokescreen for stealth maneuvers.")
        print(f"Disruptor: {self.disruptor} - Disables electronic devices and systems.")
        print(f"Remote Controller Batarang: {self.remote_controller_batarang} - Allows precision control of Batarangs.")

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Gadgets class with Batman's gadgets
    batman_gadgets = Gadgets(
        explosive_gel="High Explosive",
        smoke_pellet="Stealthy Smoke",
        disruptor="Electromagnetic",
        remote_controller_batarang="Guided Precision"
    )

    # Displaying detailed information about Batman's gadgets
    batman_gadgets.display_info()
