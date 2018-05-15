import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH = {'all':0,
         'january': 1,
         'february': 2,
         'march': 3,
         'april': 4,
         'may': 5,
         'june': 6,
         'july': 7,
         'august': 8,
         'september': 9,
         'october': 10,
         'november':11,
         'december':12}
DAYS = {'all': 0,
        'monday': 1,
        'tuesday': 2,
        'wednsday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7}

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
    invalid = 1
    while(invalid):
        city = input("Enter city name:")
        if not CITY_DATA.__contains__(city):
            print("Doesn't have this city, we only provide chicago, new york city and washington, please input again")
            invalid = 1
        else:
            invalid = 0
    # TO DO: get user input for month (all, january, february, ... , june)
    invalid = 1
    while(invalid):
        month = input("Enter month:")
        if not MONTH.__contains__(month):
            print("Doesn't have this month,please input again")
            invalid = 1
        else:
            invalid = 0
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    invalid = 1
    while(invalid):
        day = input("Enter day:")
        if not DAYS.__contains__(day):
            print("Doesn't have this day,please input again")
            invalid = 1
        else:
            invalid = 0
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
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

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
