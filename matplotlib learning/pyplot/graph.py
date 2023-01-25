# ploting a bar graph
from matplotlib import pyplot as py




'''basic one line graph'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

py.plot(x, y) #the value list of x and y axis
py.xlabel('x-axis') #the name/label of the x axis
py.ylabel('y-axis') #the name/label of the y axis

py.title('title') #the title of the bar graph
py.show() #tellin the API to show the bar graph in the screen


'''line graphs with multiple lines'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
y2 = [12, 43, 52, 12, 5, 24, 35, 34, 32, 32, 45, 32, 75, 22, 4, 56, 23, 24, 4, 2]

py.plot(x, y1, label='sales')
py.plot(x, y2, label='purchase')
py.xlabel('date') #the name/label of the x axis
py.ylabel('amount') #the name/label of the y axis

py.title('title') #the title of the bar graph
py.legend() #to show the legend table in the graph
py.show() #tellin the API to show the bar graph in the screen

'''bar graph'''
x = ['2019', '2020', '2021', '2022', '2023']
y = [1, 2, 3, 4, 5]
height = [2, 2, 3, 4, 1]

py.bar(x, height, tick_label=x, width=1, color=['red', 'yellow', 'green', 'black'])
py.xlabel('year')
py.ylabel('qty')
py.title('bar graph')
py.show()




'''histogram'''
ages = [2,5,70,40,30,45,50,45,43,40,44,
        60,7,13,57,18,90,77,32,21,20,40]
  
# setting the ranges and no. of intervals
range = (0, 100)
bins = 10  

# plotting a histogram
py.hist(ages, bins, range, color = 'green',
        histtype = 'bar', rwidth = 0.8)
  
# x-axis label
py.xlabel('age')
# frequency label
py.ylabel('No. of people')
# plot title
py.title('My histogram')
  
# function to show the plot
py.show()



'''pie chart'''
# defining labels
activities = ['eat', 'sleep', 'work', 'play']
  
# portion covered by each label
slices = [3, 7, 8, 6]
  
# color for each label
colors = ['r', 'y', 'g', 'b']
  
# plotting the pie chart
py.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
  
# plotting legend
py.legend()
  
# showing the plot
py.show()