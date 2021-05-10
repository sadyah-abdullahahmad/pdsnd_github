import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    cites=['chicago','new york city','washington']
    months=['January', 'February','March','April', 'May','All']
    days=['Monday','Tuesday','Wednesday',	'Thursday','All']

    # TO DO: get user input for city (chicago, new york city, wash ington). HINT: Use a while loop to handle invalid inputs

while True:
        city=  input('which city would you like to travel? \"Chicago\", \"New York\" or \"Washington\"? \n')
        city=city.lower()
        if city in cites:
            print('\nYou entered {}.'.format(city.title()))
            break
        else:
            print('Please Enter a valied answer')

    # TO DO: get user input for month (all, january, february, ... , june)

while True:
        month=  input ('which month would you like to travel? choose from january to june or enter All. \n')
        month=month.lower()
        if month == 'january' or month =='february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

while True:
          day=  input ('which day of week would you like to travel? choose from sundy to Wednesday or enter All. \n')
          day= day.lower()
          if day == 'monday' or day =='tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most frequent month of travel is : ',common_month)
    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most frequent day of travel is : ', common_day_of_week)
    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('the most frequent hour of travel is :', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most End Station:', common_end_station)
    # display most frequent combination of start station and end station trip
    common_start_end_station =df[['Start Station' ,'End Station']
    print('The most common start_station is:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    i = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        i = i + 5
        print(df.iloc[i:i+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break


if __name__ == "__main__":
	main()
