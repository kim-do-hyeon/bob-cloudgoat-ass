import pandas as pd

file_path = 'event_history.csv'

log_data = pd.read_csv(file_path)

log_data['Event time'] = pd.to_datetime(log_data['Event time'])

log_data = log_data.sort_values(by='Event time')

user_activity_summary = log_data.groupby('User name')['Event name'].apply(list)

log_data['Event hour'] = log_data['Event time'].dt.hour
hourly_activity = log_data.groupby('Event hour').size()

security_events = log_data[log_data['Event name'].isin([
    'CreateUser', 'DeleteTrail', 'PutEventSelectors', 'StartLogging', 'CreateTrail', 'PutBucketEncryption',
    'DeleteVpc', 'DeleteSecurityGroup', 'DeleteSubnet', 'DeleteInternetGateway'
])]


print(user_activity_summary.reset_index())

print(hourly_activity.reset_index(name='Event Count'))
print(security_events)