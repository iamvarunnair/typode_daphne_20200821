"""
[
    {
        'modla_name': ModalImpoted,
        'entries': [
            {
                'exact_field_name': 'value',
                'exact_field_name': 'value',
            },
            {
                'exact_field_name': 'value',
                'exact_field_name': 'value',
            },
            ...
        ]
    },
    ...
]
 """


def mass_insert_into_tables(input_data):
    for instance in input_data:
        if 'modal_name' in instance and 'entries' in instance and len(instance['modal_name'].objects.all()) == 0:
            for entry in instance['entries']:
                instance['modal_name'](**entry).save()
        else:
            raise Exception('modal_name and entries not in param')
