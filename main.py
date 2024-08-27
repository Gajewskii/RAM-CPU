import psutil
import matplotlib.pyplot as plt
import datetime


def CPU_RAM():
    RAM = []
    CPU = []
    RAM_percent_list = []
    
    while True:
        for _ in range(7):
            RAM_total = psutil.virtual_memory().total / (1024**3)
            RAM_available = psutil.virtual_memory().available / (1024**3)
            RAM_current = RAM_total - RAM_available
            RAM_percent = (RAM_current/RAM_total)*100
            
            CPU_current = psutil.cpu_percent(0.8)
            
            RAM.append(round(RAM_current, 1))
            RAM_percent_list.append(round(RAM_percent, 1))
            CPU.append(CPU_current)
            
            print(f"RAM usage: {round(RAM_percent, 1)} %")
            print(f"CPU usage: {CPU_current} %\n")
        
        user = input("Type 'exit' to stop, or press Enter to continue: ")
        if user == "exit":
            print(f"RAM: {RAM_percent_list}")
            print(f"CPU: {CPU}")
            break

    return RAM_percent_list, CPU

RAM_percent_list, CPU = CPU_RAM()



plt.plot([i for i in range(len(CPU))], CPU, label='CPU Usage', color='blue')
plt.plot([i for i in range(len(RAM_percent_list))], RAM_percent_list, label='RAM Usage', color='orange')


plt.title('CPU and RAM usage')
plt.xlabel('Time')
plt.ylabel('Usage (%)')
plt.grid(True)
plt.legend()

current_time = datetime.datetime.now().strftime("%d_%b_%y_%H-%M-%S")
plt.savefig(f"CPU_RAM_{current_time}.jpg")

plt.show()
import psutil
import matplotlib.pyplot as plt
import datetime
import time

def CPU_RAM():
    RAM = []
    CPU = []
    RAM_percent_list = []

    try:
        while True:
            
            RAM_total = psutil.virtual_memory().total / (1024**3)
            RAM_available = psutil.virtual_memory().available / (1024**3)
            RAM_current = RAM_total - RAM_available
            RAM_percent = (RAM_current / RAM_total) * 100

            CPU_current = psutil.cpu_percent(interval=0.8)

            
            RAM.append(round(RAM_current, 1))
            RAM_percent_list.append(round(RAM_percent, 1))
            CPU.append(CPU_current)

            
            print(f"RAM usage: {round(RAM_percent, 1)} %")
            print(f"CPU usage: {CPU_current} %\n")
            
           

    except KeyboardInterrupt:
        print("Interrupted")
        print(f"RAM: {RAM_percent_list}")
        print(f"CPU: {CPU}")

    finally:
        plot(RAM_percent_list, CPU)

def plot(RAM_percent_list, CPU):

    plt.plot([i for i in range(len(CPU))], CPU, label='CPU Usage', color='blue')
    plt.plot([i for i in range(len(RAM_percent_list))], RAM_percent_list, label='RAM Usage', color='orange')

    plt.title('CPU and RAM usage')
    plt.xlabel('Time')
    plt.ylabel('Usage (%)')
    plt.grid(True)
    plt.legend()

    
    current_time = datetime.datetime.now().strftime("%d_%b_%y_%H-%M-%S")
    plt.savefig(f"CPU_RAM_{current_time}.jpg")
   


CPU_RAM()
