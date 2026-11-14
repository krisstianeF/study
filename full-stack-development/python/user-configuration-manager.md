
# User-configuration-manager.md
```python
# add_settings(<settings dictionary>, <setting> - tuple with a key-value pair)

def add_setting(settings_dict = dict, setting = tuple):
    key = setting[0].lower()
    val = setting[1].lower()

    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings_dict[key] = val
    return f"Setting '{key}' added with value '{val}' successfully!"

def update_setting(settings_dict = dict, setting = tuple):
    #setting = tuple(i.lower() for i in setting)
    key = setting[0].lower()
    val = setting[1].lower()
    if key in settings_dict:
        settings_dict[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict = dict, key = str):
    key = key.lower()
    
    if key in settings_dict.keys():
        settings_dict.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings_dict = dict):
    if  not settings_dict:
        return 'No settings available.'

    result = 'Current User Settings:\n'
    for index, key in enumerate(settings_dict):
        result += f"{key.capitalize()}: {settings_dict[key]}\n" # key.capitalize() make first letter big
    return result


test_settings = {}
print(view_settings(test_settings))
print()

print('# Test add_setting')
print(add_setting(test_settings, ('Theme', 'light')))
print(add_setting(test_settings, ('Notifications', 'enabled')))
print(add_setting(test_settings, ('Volume', 'high')))
print(add_setting(test_settings, ('for_del', 'on')))
print()

print(view_settings(test_settings))
print()


print('# Test update_setting')
print(update_setting(test_settings, ('theme', 'dark')))
print(update_setting(test_settings, ('theeme', 'light')))
print()

print(view_settings(test_settings))
print()

print('# Test delete_setting')
print(delete_setting(test_settings, 'for_del'))
print(delete_setting(test_settings, 'for_dell'))
print()

print(view_settings(test_settings))
```
