'''
Api Reference Page Layout
'''
import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dash_table, dcc, html, State
from pages.layout_default import layout_footer, sidebar

dash.register_page(__name__, path="/docs")

docs_body = dbc.Row(
    dbc.Col([
        html.H2('Introduction', id='introduction'),
        dcc.Markdown('''
        My API is a powerful tool that allows you to access and manipulate data from our database. With this API, you can retrieve, create, update, and delete records with ease.
    '''),
        html.H2('Authentication', id='authentication'),
        dcc.Markdown('''
        To authenticate with our API, you'll need to obtain an API key. You can do this by creating an account on our website and navigating to the API section of your account settings.

        Once you have your API key, include it in the header of your requests like this:
		'''),
        dcc.Markdown('''
        ```python
        headers = {
            'Authorization': 'Bearer YOUR_API_KEY'
        }
        ```
    ''', className='markdown-code'),
        html.H2('Endpoints', id='endpoints'),
        dcc.Markdown('''
        Our API has several endpoints that you can use to interact with our data. Here's a list of the available endpoints and their supported methods:

        - `/users` (GET, POST): Retrieve a list of all users or create a new user.
        - `/users/<user_id>` (GET, PUT, DELETE): Retrieve, update, or delete a specific user by their ID.
        - `/items` (GET, POST): Retrieve a list of all items or create a new item.
        - `/items/<item_id>` (GET, PUT, DELETE): Retrieve, update, or delete a specific item by its ID.

        For more detailed information about each endpoint, including required and optional parameters and expected responses, please refer to our full documentation.
    '''),
        html.H2('Examples', id='examples'),
        dcc.Markdown('''
		Heres an example of how to use our API: \n
'''),
        dcc.Markdown('''
		```python
		import requests

		url = 'https://myapi.com/users'
		headers = {
			'Authorization': 'Bearer YOUR_API_KEY',
			'Content-Type': 'application/json'
		}

		# Example 1: Retrieve a list of all users
		response = requests.get(url, headers=headers)
		data = response.json()
		print(data)

		# Example 2: Create a new user
		data = {
			'username': 'newuser',
			'email': 'newuser@example.com',
			'password': 'password123'
		}
		response = requests.post(url, headers=headers, json=data)
		data = response.json()
		print(data)

		# Example 3: Retrieve a specific user by ID
		user_id = 123
		response = requests.get(f'{url}/{user_id}', headers=headers)
		data = response.json()
		print(data)

		# Example 4: Update a specific user by ID
		user_id = 123
		data = {
			'username': 'updateduser',
			'email': 'updateduser@example.com',
			'password': 'newpassword'
		}
		response = requests.put(f'{url}/{user_id}', headers=headers, json=data)
		data = response.json()
		print(data)

		# Example 5: Delete a specific user by ID
		user_id = 123
		response = requests.delete(f'{url}/{user_id}', headers=headers)
		data = response.json()
		print(data)
		```

    ''', className='markdown-code'),
        html.H2('Error Handling', id='error-handling'),
        dcc.Markdown('''
	Our API uses standard HTTP status codes to indicate the success or failure of a request. In general, codes in the 2xx range indicate success, codes in the 4xx range indicate an error on the client side (e.g. a missing or invalid parameter), and codes in the 5xx range indicate an error on the server side.

	In the event of an error, our API will return a JSON object with more detailed information about the error. Here are some examples of error responses:
	'''
                     ),
        dcc.Markdown('''
	If you receive a `429 Too Many Requests` response, you have exceeded the rate limit for that endpoint. In this case, you should wait for the specified amount of time before making another request to that endpoint.

	To help you stay within the rate limits, our API includes `X-RateLimit-Remaining` and `X-RateLimit-Reset` headers in the response. These headers indicate how many requests you have left for the current time window and when the rate limit will reset, respectively.
'''),
        html.H2('Rate Limits', id='rate-limits'),
        dcc.Markdown('''
       Our API enforces rate limits to ensure fair usage and prevent abuse. Each endpoint has its own rate limit, which is specified in our full documentation.

       If you exceed the rate limit for an endpoint, you will receive a `429 Too Many Requests` response. In this case, you should wait for the specified amount of time before making another request to that endpoint.

       To help you stay within the rate limits, our API includes `X-RateLimit-Remaining` and `X-RateLimit-Reset` headers in the response. These headers indicate how many requests you have left for the current time window and when the rate limit will reset, respectively.
    ''')
    ], className='mx-6'))

docs_nav = dbc.Col([
    html.H2('API Reference', className='nav-title'),
    html.Ul([
        html.Li(html.A('Introduction', href='#introduction',
                       className='scroll-link side-nav-item')),
        html.Li(html.A('Authentication', href='#authentication',
                       className='scroll-link side-nav-item')),
        html.Li(html.A('Endpoints', href='#endpoints',
                       className='scroll-link side-nav-item')),
        html.Li(html.A('Examples', href='#examples',
                       className='scroll-link side-nav-item')),
        html.Li(html.A('Error Handling', href='#error-handling',
                       className='scroll-link side-nav-item')),
        html.Li(html.A('Rate Limits', href='#rate-limits',
                       className='scroll-link side-nav-item'))
    ])
], id="docs-nav",
    style={'border-right': '0px solid #ddd', 'margin-left': '20rem', 'margin-top': '0rem', 'position': 'fixed'})

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    dbc.Row([
        docs_nav,
        docs_body,
    ], style={'margin-top': '1rem', 'width': '99%'}),
    layout_footer
])
