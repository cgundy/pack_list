import click
from clothes import Clothes    


def pack(class_category, conditions):
    pack_list = []
        
    item_list = class_category.__subclasses__()

    for item in item_list:
        quantity = item.get_quantity(conditions)
        if quantity > 0:
            pack_list.append((item.__name__, quantity))

    return pack_list


@click.command()
def get_conditions():

    conditions = {}

    conditions['name'] = click.prompt('Trip to plan for')
    conditions['days'] = click.prompt('How many days are you traveling for?', type=int, prompt_suffix=' ')
    conditions['packsize'] = click.prompt('How big will your luggage size be? Options are: small, medium or large.',
                            type=str, prompt_suffix=' ')
    conditions['can_wash'] = click.prompt('Will you have access to a washer and dryer during the trip?',
                            type=bool, prompt_suffix=' ')
    conditions['weather'] = click.prompt('What will the temperature be most days? Options are: cold, mild or hot.',
                            type=str, prompt_suffix=' ')
    conditions['store_available'] = click.prompt('Will there be access to convenience stores where you are?',
                            type=bool, prompt_suffix=' ')
    conditions['outdoors'] = click.prompt('Will you be spending a significant time outdoors?',
                            type=bool, prompt_suffix=' ')
    conditions['indoors'] = click.prompt('Will you be spending a significant time indoors?',
                            type=bool, prompt_suffix=' ')
    conditions['will_work'] = click.prompt('Will you be working during your trip?',
                            type=bool, prompt_suffix=' ')
    conditions['travel_alone'] = click.prompt('Will you be traveling alone?',
                            type=bool, prompt_suffix=' ')


def create_pack_list():
    conditions = {
        'days':5,
        'weather':'mild'
    }
    clothes = pack(Clothes, conditions)
    print(clothes)

if __name__ == '__main__':
    create_pack_list()
    
    
