import click
from categories.clothes import Clothes
from categories.electronics import Electronics

def pack(class_category, conditions):
    '''Determine which items needs to be packed within a given category.
    Returns: a list of tuples with the specific item and its quantity'''

    pack_list = []
    item_list = class_category.__subclasses__()

    for item in item_list:
        quantity = item(conditions).get_quantity()
        if item.__name__ not in ['Ipad', 'Laptop']:
            quantity = class_category(conditions).adjust_quantity(quantity)
        if quantity > 0:
            pack_list.append((item.__name__, quantity))

    return pack_list

@click.group()
def cli():
    pass


def get_conditions():
    conditions = {}
    conditions['name'] = click.prompt('Trip to plan for')
    conditions['days'] = click.prompt('How many days are you traveling for?', type=int, prompt_suffix=' ')
    conditions['can_wash'] = click.prompt('Will you have access to a washer and dryer during the trip?',
                            type=bool, prompt_suffix=' ')
    conditions['weather'] = click.prompt('What will the temperature be most days? Options are: cold, mild or hot.',
                            type=str, prompt_suffix=' ')
    conditions['store_available'] = click.prompt('Will there be access to convenience stores where you are?',
                            type=bool, prompt_suffix=' ')
    conditions['outdoors'] = click.prompt('Will you be spending a significant time outdoors?',
                            type=bool, prompt_suffix=' ')
    conditions['downtime'] = click.prompt('Will you have a lot of downtime?',
                            type=bool, prompt_suffix=' ')
    conditions['will_work'] = click.prompt('Will you be working during your trip?',
                            type=bool, prompt_suffix=' ')
    conditions['travel_alone'] = click.prompt('Will you be traveling alone?',
                            type=bool, prompt_suffix=' ')
    return conditions


def generate_test_conditions():
    conditions = {
        'name':'test',
        'days':4,
        'weather':'hot',
        'can_wash': True,
        'store_available': True,
        'outdoors' : True,
        'downtime': True,
        'will_work': True,
        'travel_alone': True
    }
    return conditions


@cli.command()
@click.option('--input', default='user')
def create_pack_list(input):
    if input == 'test':
        travel_conditions = generate_test_conditions()
    elif input == 'user':
        travel_conditions = get_conditions()
    clothes = pack(Clothes, travel_conditions)
    electronics = pack(Electronics, travel_conditions)
    print(clothes)
    print(electronics)

if __name__ == '__main__':
    cli()
    
