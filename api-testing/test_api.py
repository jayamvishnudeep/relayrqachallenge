#  -*- coding: utf-8 -*-

from __future__ import unicode_literals
import requests
import pytest


@pytest.mark.ZomatoTC_001
def test_zomato_get_cities_endpoint_for_mumbai():
    """ Verify GET End Point 'Cities' is working as expected when city name is given as Mumbai """

    zomato_get_cities_endpoint = 'https://developers.zomato.com/api/v2.1/cities?q=mumbai'

    rp = requests.get(zomato_get_cities_endpoint, headers={"user-key": "3fcb81109ef264e19e629e1568bca526"})

    response = (rp.json())

    assert rp.status_code == 200
    assert response['location_suggestions'][0]['id'] == 3
    assert response['location_suggestions'][0]['name'] == 'Mumbai'
    assert response['location_suggestions'][0]['country_id'] == 1
    assert response['location_suggestions'][0]['country_name'] == 'India'
    assert response['location_suggestions'][0][
               'country_flag_url'] == 'https://b.zmtcdn.com/images/countries/flags/country_1.png'
    assert response['location_suggestions'][0]['state_name'] == ''
    assert response['location_suggestions'][0]['state_code'] == ''
    assert response['status'] == 'success'
    assert response['user_has_addresses'] is True


@pytest.mark.ZomatoTC_002
def test_zomato_get_cities_endpoint_for_newyork():
    """ Verify GET End Point 'Cities' is working as expected when city name is given as NewYork """

    zomato_get_cities_endpoint = 'https://developers.zomato.com/api/v2.1/cities?q=NewYork'

    rp = requests.get(zomato_get_cities_endpoint, headers={"user-key": "3fcb81109ef264e19e629e1568bca526"})

    response = (rp.json())

    assert rp.status_code == 200
    assert response['location_suggestions'][0]['id'] == 280
    assert response['location_suggestions'][0]['name'] == 'New York City, NY'
    assert response['location_suggestions'][0]['country_id'] == 216
    assert response['location_suggestions'][0]['country_name'] == 'United States'
    assert response['location_suggestions'][0][
               'country_flag_url'] == 'https://b.zmtcdn.com/images/countries/flags/country_216.png'
    assert response['location_suggestions'][0]['state_name'] == 'New York State'
    assert response['location_suggestions'][0]['state_code'] == 'NY'
    assert response['location_suggestions'][2]['id'] == 5188
    assert response['location_suggestions'][2]['name'] == 'New York, IL'
    assert response['location_suggestions'][2]['state_name'] == 'Illinois'
    assert response['status'] == 'success'
    assert response['user_has_addresses'] is True


@pytest.mark.ZomatoTC_003
@pytest.mark.parametrize("cityname,status_code",
                         [
                             ('Bengaluru', 200),
                             ('Sydney', 200),
                             ('warsaw', 200),
                             ('Istanbul', 200)
                         ]
                         )
def test_zomato_get_cities_endpoint_for_multiple_cities(cityname, status_code):
    """ Verify GET End Point 'Cities' is working as expected when city name is given in parameterized format """

    zomato_get_cities_endpoint = 'https://developers.zomato.com/api/v2.1/cities?q={}'.format(cityname)

    rp = requests.get(zomato_get_cities_endpoint, headers={"user-key": "3fcb81109ef264e19e629e1568bca526"})

    response = (rp.json())

    assert rp.status_code == status_code
    assert response['status'] == 'success'
    assert response['user_has_addresses'] is True


@pytest.mark.ZomatoTC_004
def test_zomato_get_cities_endpoint_without_providing_apikeys():
    """ Verify GET End Point is working as expected when API key is not added to header when the endpoint is called
     """

    zomato_get_cities_endpoint = 'https://developers.zomato.com/api/v2.1/cities?q=mumbai'

    rp = requests.get(zomato_get_cities_endpoint)

    response = (rp.json())

    assert rp.status_code == 403
    assert response['status'] == 'Forbidden'
    assert response['message'] == 'Invalid API Key'


@pytest.mark.reqresTC_001
def test_create_new_user_endpoint():
    """ Verify POST End Point of 'Create new user' is working as expected """

    create_new_user = 'https://reqres.in/api/users'

    data = {

        "name": 'Vishnu',
        "job": 'QA Engineer'

    }

    rp = requests.post(create_new_user, json=data)

    response = (rp.json())

    assert rp.status_code == 201
    assert response['name'] == 'Vishnu'
    assert response['job'] == 'QA Engineer'


@pytest.mark.reqresTC_02
def test_update_existing_user_endpoint():
    """ Verify PUT End Point of Existing User is working as expected """

    update_user_url = 'https://reqres.in/api/users/2'

    data = {

        "name": 'Vishnudeep Jayam',
        "job": 'QA Automation Engineer'

    }

    rp = requests.put(update_user_url, json=data)

    response = (rp.json())

    assert rp.status_code == 200
    assert response['name'] == 'Vishnudeep Jayam'
    assert response['job'] == 'QA Automation Engineer'


@pytest.mark.reqresTC_003
def test_delete_existing_user_endpoint():
    """ Verify PUT End Point of Existing User is working as expected """

    update_user_url = 'https://reqres.in/api/users/2'

    rp = requests.delete(update_user_url)
    assert rp.status_code == 204
