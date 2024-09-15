import tkinter as tk

class MenorahApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menorah")
        
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.branches = []
        self.lights = []
        
        self.create_menorah()

    def create_menorah(self):
        # Create 8 branches and clickable spots at the top
        for i in range(8):
            # Calculate x position for each branch
            x = 50 + i * 70
            # Draw branch
            self.canvas.create_line(x, 300, x, 200, width=5)
            # Create clickable light at the top
            light = self.canvas.create_oval(x-10, 190, x+10, 210, fill="gray", tags=f"light_{i}")
            self.lights.append(light)
            self.canvas.tag_bind(light, "<Button-1>", lambda event, index=i: self.light_candle(index))
    
    def light_candle(self, index):
        # Change the color of the light to yellow when clicked (to represent lighting the candle)
        self.canvas.itemconfig(self.lights[index], fill="yellow")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenorahApp(root)
    root.mainloop()

