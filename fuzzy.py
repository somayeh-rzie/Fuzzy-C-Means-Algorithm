import csv
from random import randrange
import math
import matplotlib.pyplot as plt 

path1 = "data1.csv"
path2 = "data2.csv"
path3 = "data3.csv"
path4 = "data4.csv"

m =2

data = []
points = []


def create_centers(r):
    centers = [0 for i in range(r)]
    return centers


def increase(r):
    return r+1


#read the csv file
def read_file(filePath):

    with open(filePath , 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


#find random centroids for the first step
def first_step(data , c):

    centers = create_centers(c)

    for i in range(c):

        r = randrange(len(data))
        centers[i] = data[r]
    return centers
    # print(centers)


#calculate euclidian distance between two points
def euclidean_distance(x1,x2,v1,v2):

    a = float(x1)-float(v1)
    b = float(x2)-float(v2)
    sum = math.pow(a,2) + math.pow(b,2)
    return math.sqrt(sum)


#reinitialize the array to 0
def reset_to_0(array):
    for i in range(len(array)):
        array[i] = 0


#find the index of maximum element
def find_max(arr):
    temp = 0
    for it in range(len(arr)):
        if(arr[it] > temp) :
            temp = it
    return(temp)



def func(data ,centers ,c ,m):

    l = len(data)

    global dependency

    dependency = [[0 for i in range(c)] for j in range(l)]

    power = 2.0 / (m-1)
    sum = 0
    flag = 0
    

    for p in range(100):
        cost = 0
        X=0
        Y=0
        center_denominator = 0

        for i in range(c):

            flag =0

            (v1 , v2) = centers[i]
            v1 = float(v1)
            v2 = float(v2)

            for k in range(l-1):

                (x1 , x2) = data[k]
                x1 = float(x1)
                x2 = float(x2)

                face = euclidean_distance(x1,x2,v1,v2)
                # print(face)

                # print('hello')

                if(face == 0):
                    dependency[k][i]=1
                    flag = 1
                    break
                
                else :

                    for j in range (c):

                        # print(j)
                        (w1 , w2) = centers[j]
                        w1 = float(w1)
                        w2 = float(w2)
                        denominator = euclidean_distance(x1,x2,w1,w2)
                
                        if(denominator == 0):
                            dependency[k][j] = 1
                            flag = 1
                            break

                        sum += pow((face/denominator),power)

                if(flag == 0):    
                    dependency[k][i] = 1.0/sum

                # print(dependency[k][i])

                weight_pow = float(pow(dependency[k][i], m))

                center_denominator += weight_pow
                
                X += (weight_pow*x1)
                Y += (weight_pow*x2)

                distance = euclidean_distance(x1 ,x2 ,v1 ,v2)

                cost += weight_pow*pow(distance,2)

            centers[i] = (X/center_denominator , Y/center_denominator)

                
        # print(cost)
    return cost , dependency
        
    # print(len(V))



def plot_variableC():

    x=[]
    y=[]

    c=1
    m=2

    for i in range(10):
        centers = first_step(data ,c)
        cost,dependency = func(data ,centers ,c ,m)
        # print(cost)
        x.append(c)
        y.append(cost)
        c = increase(c)
    plt.xlabel("C (Number of Clusters)")
    plt.ylabel("Cost")
    plt.title("Fuzzy C-Means Clustering")
    plt.plot(x,y)
    plt.show()




def plot_variableM():
    x=[]
    y=[]

    c=3
    m=2

    for i in range(10):
        centers = first_step(data ,c)
        cost , dependency = func(data ,centers ,c ,m)
        # print(cost)
        x.append(c)
        # print(c)
        y.append(cost)
        m = increase(m)
    plt.xlabel("C (Number of Clusters)")
    plt.ylabel("Cost")
    plt.title("Fuzzy C-Means Clustering")
    plt.plot(x,y)
    plt.show()




def colorFul_plot():

    c=3
    m=2

    centers = first_step(data ,c)
    clusters = [0 for i in range(len(data))]

    cost , dependency = func(data ,centers ,c ,m)

    for k in range(len(data)):
        (x1,x2) = data[k]
        clusters[k] = find_max(dependency[k])

        if(dependency[k] == 0):
            plt.plot(x1, x2, col = "red")
        if(dependency[k] == 1):
            plt.plot(x1, x2, col = "blue")
        if(dependency[k] == 0):
            plt.plot(x1, x2, col = "green")
    plt.show()




def main():

    data = read_file(path3)
    clusters = [[0 for i in range(2)] for j in range(len(data))]
    plot_variableC()
    # plot_variableM()
    # colorFul_plot()


if __name__ == "__main__":
    main()