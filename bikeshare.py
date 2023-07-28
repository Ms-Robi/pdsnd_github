import time
import sys
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
         city = input("Enter city, choose between chicago, new york city, washington: ")
         if city.lower() in ["chicago", "new york city", "washington"]: break
         else:
            print("Invalid city. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
         month = input("Enter month, choose among [All, January, February, March, April, May, June]: ")
         if month.title() in ["all","January", "February", "March", "April", "May", "June"]:
            break
         else:
            print("Invalid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         day = input("Enter day, choose among [All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
         if day.title() in ["All","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]: 
            break
         else:
            print("Invalid day_of_week. Please try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    elif city == 'washington': 
        df = pd.read_csv('washington.csv')
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month is {}'.format(most_common_month))
    

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    most_common_day = df['day'].mode()[0]
    print('Most common day is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common start hour is {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startStation =  df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is {}'.format(most_common_startStation))

    # TO DO: display most commonly used end station
    most_common_endStation =  df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is {}'.format(most_common_endStation))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_and_End Station'] = df['Start Station'] +' '+ df['End Station']
    most_frequent_trip = df['Start_and_End Station'].value_counts().idxmax()
    print('The most frequent combination of start and end station is {}'.format(most_frequent_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    total_travel_time = df['End Time'] - df['Start Time']
    print('Total travel time is {}'.format(total_travel_time.sum()))

    # TO DO: display mean travel time
    mean_travel_time = total_travel_time.mean()
    print('The mean travel time is {}'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
    # TO DO: Display counts of user types
      user_type_count = df.groupby('User Type').size()
      print('User type count')
      print()
      print(user_type_count)

    # TO DO: Display counts of gender
      gender = df.groupby('Gender').size()
      print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
      print("Birth date Data")
      earliest_birth_year = df['Birth Year'].min()
      most_recent_birthyear = df['Birth Year'].max()
      most_common_birthyear = df['Birth Year'].mode()[0]
      print("Earliest birth year {}".format(earliest_birth_year))
      print("Most recent birth year {}".format(most_recent_birthyear))
      print("Most common birth year {}".format(most_common_birthyear))
    else:
      print("Gender and User Type information not found")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
def display_data(df):
    row_input = input('\nWould you like to view rows of individual trip data? Enter yes or no \n')
    if row_input.lower() == 'yes':
       view_data_choice = True
       start = 0
       while view_data_choice:
            try: 
                rows = input('How many rows do you want displayed? ')
                num_of_rows = int(rows)
                print(df.iloc[start:num_of_rows+start])
                start += num_of_rows
                view_data = input("Do you wish to continue?: yes or no: ").lower()
                if view_data == "yes":
                    view_data_choice  = True
                else:
                   view_data_choice = False
                   break
            except ValueError:
              print("Invalid input, please try again")
                
      


if __name__ == "__main__":
	main()