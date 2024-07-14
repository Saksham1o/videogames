import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from matplotlib import style 
df = pd.read_csv('C:\\Users\\gulsh\\OneDrive\\Coding\\python\\ip project\\vgsales1.csv')
nrow,ncol = df.shape 
print("==================================================================================================================")
print('                                         Analysis Tool for Video Game Sales                                      |')
print("==================================================================================================================")
print()
print('Printing the dataframe:')
print(df.head()) # displaying first 5 rows
print(f'There are {nrow} rows and {ncol} columns')
print()
ch=input('Enter (A) for dataframe questions and (B) for visual representation of data:')
while ch=='A' or ch=='a':
    # questions to be asked
    print()
    print('1. Which region has performed the best in terms of sales?')
    print('2. Which platform is most famous?')
    print('3. which genre is most famous in terms of sales?')
    print('4. which publisher is most famous in terms of sales?')
    print('5. which year has performed the best in terms of sales?')
    print('6. which year has performed the worst in terms of sales?')
    print('7. What are the top 10 games currently making the most sales globally?')
    print('8. What are the top 10 games currently making the least sales globally?')
    print('9. What are the top games for NA region?')
    print('10.Display the year and platform used recently for highest sales?')
    print()
    choice=int(input('Enter your choice no from above questions:'))
    if choice==1:
        a=(df['NA_Sales'].mean())
        b=(df['EU_Sales'].mean())
        c=(df['JP_Sales'].mean())
        d=(df['Other_Sales'].mean())
        e=(df['Global_Sales'].mean())
        if a>b and a>c and a>d and a>e:
            print('NA region has performed the best in terms of sales')
        elif b>a and b>c and b>d and b>e:
            print('EU region has performed the best in terms of sales')
        elif c>a and c>b and c>d and c>e:
            print('JP region has performed the best in terms of sales')
        elif d>a and d>b and d>c and d>e:
            print('Other region has performed the best in terms of sales')
        else:
            print('Global region with',e,' has performed the best in terms of sales')
    elif choice==2:
        print('The Best Platform is :')
        print(df['Platform'].value_counts().idxmax())
    elif choice==3:
        print('The Best Genre is :')
        print(df['Genre'].value_counts().idxmax())
    elif choice==4:
        print('The Best Publisher is :')
        print(df['Publisher'].value_counts().idxmax())
    elif choice==5:
        print('The Best Year is :')
        print(df['Year'].value_counts().idxmax())
    elif choice==6:
        print('The Worst Year is :')
        print(df['Year'].value_counts().idxmin())
    elif choice==7:
        print('The top 10 games currently making the most sales globally are :')
        ac = df['Global_Sales'].nlargest(10).index
        ch7 = df.iloc[ac][['Name','Global_Sales']]
        print(ch7)
    elif choice==8:
        print('The top 10 games currently making the least sales globally are :')
        ad = df['Global_Sales'].nsmallest(10).index
        ch8 = df.iloc[ad]['Name']
        print(ch8)
    elif choice==9:
        print('The top games for NA regions are :')
        top_na_games = df.sort_values('NA_Sales', ascending=False).head()['Name']
        print(top_na_games)
    elif choice==10:
        print('The year and platform used recently for highest sales are :')
        a = df['Year'].idxmax()
        print(df.iloc[a][['Year','Platform']])
    else:
        print('choice not found pls enter between 1-10')
    print()
    choice=input('do you want to continue yes/no:')
    if choice=='no':
        c = input('Do you want to switch to visual representation of data? yes/no:')
        if c=='yes':
            ch = 'B'
        else:
            break
    else:
        continue
while ch=='B' or ch=='b':
    # visual representation
    print("==============================================================================================================")
    print('                                       Visual Representation Of Data                                         |')
    print("==============================================================================================================")
    print()
    print('1.what was the trend of global video game sales between 2000 and 2005?')
    print('2.What were the global sales numbers of the most popular platform during \
          the same period?')
    print('3.Plot Top 10 games globally in pie chart.')
    print('4.What are the top gaming genres that are making high sales?')
    print('5.Plot the Sales of the games for each platform on a pie chart.')
    print('6.Create a histogram to show the distribution of Global Sales across all games')
    print('7.Show the comparison of Global Sales between different genres for a \
           specific publisher across different platforms.')
    print('8.Plot the Rank against the Name of the games on a line chart')
    print('9.Plot the Rank against the Name of the games on a bar chart')
    print('10.Create a bar chart to show the comparison of Global Sales between different \
          genres for a specific publisher across different platforms and years')
    print()
    choice=int(input('Enter your choice no from the above questions:'))
    if choice==1:
        x = [2000,2001,2002,2003,2004,2005]
        y = [50,10,70,90,30,50]
        pl.figure(figsize=(6,5))
        pl.xlabel('Years',fontdict={'fontsize':15,'color':'blue',
                                    'fontweight':'bold'})
        pl.ylabel('Global Sales',fontdict={'fontsize':15,'color':'green',
                                           'fontweight':'bold'})
        pl.title('Global sales of video games from 2000 to 2005',
                 fontdict={'fontsize':15,'color':'purple','fontweight':'bold'})
        style.use('ggplot')
        pl.xticks(x)
        pl.yticks(y)
        d = input('Enter (b) for bar chart and (l) for line chart:')
        if d=='b' or d=='B':
            pl.bar(x,y,color='skyblue',edgecolor='black')
            pl.grid(axis='x', linestyle='--', color='grey')
        elif d=='l' or d=='L':
            pl.plot(x,y,'o--')
        pl.show()
    elif choice==2:
        print()
        print('The best platform is : ',df['Platform'].value_counts().idxmax())
        x = [2000,2001,2002,2003,2004,2005]
        y = [30.1,24.4,12.6,40.6,10.0,17.0]
        pl.figure(figsize=(6,5))
        pl.xlabel('Years',fontdict={'fontsize':15,'color':'blue','fontweight':'bold'})
        pl.ylabel('Global Sales of DS Platform',
                  fontdict={'fontsize':15,'color':'green','fontweight':'bold'})
        pl.title('Global sales of DS platform from 2000 to 2005',
                 fontdict={'fontsize':15,'color':'purple','fontweight':'bold'})
        pl.xticks(x)
        pl.yticks(range(0,51,10))
        d = input('Enter (b) for bar chart and (l) for line chart:')
        if d=='b' or d=='B':
            pl.bar(x,y,color='red',edgecolor='yellow')
            #pl.grid(axis='x',linestyle='--',color='purple')
        elif d=='l' or d=='L':
            pl.plot(x,y,'r--')
        pl.show()
    elif choice==3:
        print()
        ac = df['Global_Sales'].nlargest(10).index
        ch7 = df.iloc[ac][['Name','Global_Sales']]
        pie1 = px.pie(ch7, values=ch7['Global_Sales'][:10], 
                      names=ch7['Name'][:10],title='Top 10 games globally', 
              color_discrete_sequence=px.colors.sequential.Purp_r)
        pie1.update_traces(textposition='inside', textinfo='percent+label',showlegend=False)
        pie1.show()
    elif choice==4:
        print()
        genre_df = df.groupby("Genre")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index()
        print(genre_df) #print the dataframe
        bar_genre= px.bar(genre_df, x='Genre', y='Global_Sales',color='Global_Sales',color_continuous_scale='Burgyl')
        bar_genre.show()
    elif choice==5:
        print()
        pl.figure(figsize=(8,8))
        df['Platform'].value_counts().nlargest(10).plot(kind='pie', autopct='%1.1f%%')
        pl.title('Sales of Games for Each Platform',
                 fontdict={'fontsize':20,'color':'purple','fontweight':'bold'})
        pl.show()
    elif choice==6: 
        pl.figure(figsize=(10,6))
        df['Global_Sales'].hist(bins=50)
        pl.xlabel('Global Sales',
                  fontdict={'fontsize':15,'color':'brown','fontweight':'bold'})
        pl.ylabel('Frequency',
                  fontdict={'fontsize':15,'color':'green','fontweight':'bold'})
        pl.xlim(0, 5)
        pl.title('Distribution of Global Sales',
                 fontdict={'fontsize': 15, 'color': 'purple', 'fontweight': 'bold'})
        pl.show()
    elif choice==7:
        print()
        df_filtered = df[df['Publisher']=='Sony Computer Entertainment'].nlargest(10 ,'Global_Sales')
        grouped_data = df_filtered.groupby(["Genre", "Platform"])["Global_Sales"].sum()
        print(grouped_data)
        unstacked_data = grouped_data.unstack(fill_value=0)
        fig, ax = pl.subplots(figsize=(10, 8))
        ch = input('Enter (b) for bar chart and (l) for line chart:')
        if ch=='b' or ch=='B':
            unstacked_data.plot(kind="bar", stacked=True, colormap="tab20", ax=ax)
        elif ch=='l' or ch=='L':
            unstacked_data.plot(kind="line", ax=ax)
        pl.xlabel("Platform")
        pl.ylabel("Global Sales")
        pl.title("Global Sales Comparison by Genre and Platform for Sony Computer Entertainment",
                  fontdict={'fontsize': 15, 'color': 'purple', 'fontweight': 'bold'})
        pl.legend(title="Genre - Platform", loc="upper left", bbox_to_anchor=(1.05, 1))
        pl.xticks(rotation=45, ha="right")
        pl.tight_layout()
        pl.show()
    elif choice==8:
        print()
        x = df['Global_Sales'].nlargest(10)
        y = df['Rank'].nlargest(10)
        pl.figure(figsize=(6,5))
        ch = input('Enter (s) for scatter plot and (l) for line plot:')
        if ch=='s' or ch=='S':
            pl.scatter(x,y,c='red',edgecolor='yellow')
        elif ch=='l' or ch=='L':
            pl.plot(x,y,color='red')
        pl.xlabel('Global Sales',fontdict={'fontsize':15,'color':'blue','fontweight':'bold'})
        pl.ylabel('Rank',fontdict={'fontsize':15,'color':'green','fontweight':'bold'})
        pl.title('Rank vs Global Sales',fontdict={'fontsize':15,'color':'purple','fontweight':'bold'})
        pl.show()
    elif choice==9:
        print()
        # Adjust figure size for better spacing (optional)
        pl.figure(figsize=(10, 6))  # Adjust figure size
        pl.bar(df['Name'].head(), df['Rank'].head(),color='k',edgecolor='yellow',
               linewidth=4)
        pl.xlabel('Games Names', 
                  fontdict={'fontsize': 15, 'color': 'blue', 'fontweight': 'bold'})
        pl.ylabel('Games Rank', 
                  fontdict={'fontsize': 15, 'color': 'green', 'fontweight': 'bold'})
        pl.title('Rank of Games', 
                 fontdict={'fontsize': 15, 'color': 'purple', 'fontweight': 'bold'})
        pl.xticks(rotation=45, ha='right')
        pl.grid(axis='x', linestyle='--', color='grey')
        pl.show()
    elif choice==10:
        print()
        df_filtered = df[df['Publisher']=='Microsoft Game Studios'].nlargest(10 ,'Global_Sales')
        grouped_data = df_filtered.groupby(["Genre", "Platform", "Year"])["Global_Sales"].sum()
        print(grouped_data)
        unstacked_data = grouped_data.unstack(fill_value=0)
        fig, ax = pl.subplots(figsize=(10, 8))
        unstacked_data.plot(kind="bar", stacked=True, colormap="tab20", ax=ax)
        pl.xlabel("Year")
        pl.ylabel("Global Sales")
        pl.title("Global Sales Comparison by Genre and Platform for Microsoft Game Studios", 
                 fontdict={'fontsize': 15, 'color': 'purple', 'fontweight': 'bold'})
        pl.legend(title="Genre - Platform", loc="upper left", bbox_to_anchor=(1.05, 1))
        pl.xticks(rotation=45, ha="right")
        pl.tight_layout()
        pl.show()
    else:
        print('choice not found pls enter between 1-10')
    choice=input('do you want to continue yes/no:')
    if choice=='no':
        break
    else:
        continue
while ch!='A' and ch!='a' and ch!='B' and ch!='b':
    print('Choice not found !!!!!')
    break