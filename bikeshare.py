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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("common month:%d" % common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("common day:%d" % common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("common hour:%d" % common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station    
    print("common used start station:%s" % (df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("common used end station:%s" % (df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    #df.groupby(['ITEM', 'CATEGORY']).apply(pd.DataFrame.mode).reset_index(drop=True)
    #df.groupby('a').agg(lambda x: np.mean(pd.Series.mode(x))).reset_index()
    common_combined = df.groupby(['Start Station','End Station'])
    #print("most frequent combination of start station and end station trip:%s" % common_combined.apply(pd.DataFrame.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time: %d" % df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("mean travel time: %d" % df['Trip Duration'].mean())

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
