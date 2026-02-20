import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['all', 'january', 'february', 'march',
          'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


# -------------------------------------------------
# FILTER INPUT
# -------------------------------------------------
def get_filters():

    print("Hello! Let's explore some US bikeshare data!")

    # ----- CITY -----
    while True:
        city = input(
            "\nWould you like to see data for Chicago, New York City, or Washington?\n"
        ).lower().strip()

        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    # ----- FILTER TYPE -----
    filter_types = ['month', 'day', 'both', 'not at all']

    while True:
        filter_type = input(
            "\nHow would you like to filter the data?\n"
            "Type: Month, Day, Both, or Not at all\n"
        ).lower().strip()

        if filter_type in filter_types:
            break
        else:
            print("Invalid choice. Please try again.")

    # Defaults
    month = 'all'
    day = 'all'

    # ----- MONTH -----
    if filter_type in ['month', 'both']:
        while True:
            month = input(
                "\nWhich month? (January,Feruary,March,April,May,June)\n"
            ).lower().strip()

            if month in MONTHS[1:]:
                break
            else:
                print("Invalid month. Please try again.")

    # ----- DAY -----
    if filter_type in ['day', 'both']:
        while True:
            day = input(
                "\nWhich day? (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday, Sunday)\n"
            ).lower().strip()

            if day in DAYS[1:]:
                break
            else:
                print("Invalid day. Please try again.")

    print("-" * 40)
    return city, month, day


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract time components
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        month_index = MONTHS.index(month)
        df = df[df['month'] == month_index]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df


# -------------------------------------------------
# TIME STATS
# -------------------------------------------------
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most Common Month:",
          MONTHS[df['month'].mode()[0]].title())

    print("Most Common Day:",
          df['day_of_week'].mode()[0])

    print("Most Common Start Hour:",
          df['hour'].mode()[0])

    print("\nThis took %s seconds."
          % (time.time() - start_time))
    print('-' * 40)


# -------------------------------------------------
# STATION STATS
# -------------------------------------------------
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most Common Start Station:",
          df['Start Station'].mode()[0])

    print("Most Common End Station:",
          df['End Station'].mode()[0])

    df['Trip'] = df['Start Station'] + " → " + df['End Station']

    print("Most Frequent Trip:",
          df['Trip'].mode()[0])

    print("\nThis took %s seconds."
          % (time.time() - start_time))
    print('-' * 40)


# -------------------------------------------------
# TRIP DURATION
# -------------------------------------------------
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total Travel Time:",
          df['Trip Duration'].sum())

    print("Average Travel Time:",
          df['Trip Duration'].mean())

    print("\nThis took %s seconds."
          % (time.time() - start_time))
    print('-' * 40)


# -------------------------------------------------
# USER STATS
# -------------------------------------------------
def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("User Types:\n",
          df['User Type'].value_counts())

    # Gender
    if 'Gender' in df.columns:
        print("\nGender Counts:\n",
              df['Gender'].value_counts())
    else:
        print("\nGender data not available.")

    # Birth Year
    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:",
              int(df['Birth Year'].min()))
        print("Most Recent Birth Year:",
              int(df['Birth Year'].max()))
        print("Most Common Birth Year:",
              int(df['Birth Year'].mode()[0]))
    else:
        print("\nBirth year data not available.")

    print("\nThis took %s seconds."
          % (time.time() - start_time))
    print('-' * 40)


# -------------------------------------------------
# RAW / INDIVIDUAL TRIP DATA
# -------------------------------------------------
def display_raw_data(df):

    show_data = input(
        "\nWould you like to view individual trip data? Enter yes or no:\n"
    ).lower().strip()

    start_loc = 0

    while show_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5

        show_data = input(
            "\nWould you like to view 5 more rows of individual trip data? Enter yes or no:\n"
        ).lower().strip()


# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():

    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input(
            "\nWould you like to restart? Enter yes or no.\n"
        ).lower().strip()

        if restart != 'yes':
            print("\nExiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
