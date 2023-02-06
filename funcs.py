import re
import matplotlib.pyplot as plt

def check_email (name:str,email:str) -> bool:
    '''
    Function to check and save the email
    '''
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,email):
        with open("emails.txt","a+",encoding="utf-8") as savefile:
            string = f"{name}:{email}"
            savefile.seek(0)
            if string.lower() in savefile.read().lower():
                pass
            else:
                savefile.write(string + "\n")
                return True
    else:
        return False

def calculate_metrics (age:int,height:float,weight:float,gender:str):
    '''
    Function to calculate the metrics
    '''
    
    gender_type = 1 if gender =="Male" else 0
    bmi = weight/(height*height)
    body_fat = 1.2*bmi + 0.23*age -10.8*gender_type -5.4
    return bmi,body_fat


def plot_body_fat (body_fat:float):
    
    labels = ["Fat","Rest"]
    sizes = [body_fat,100-body_fat]
    explode = (0.1,0)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    
    return fig1