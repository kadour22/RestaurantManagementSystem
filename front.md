
http://127.0.0.1:8000/MenuItem/  GET CREATE RETRIEVE

http://127.0.0.1:8000/Restaurant/  GET CREATE RETRIEVE
http://127.0.0.1:8000/Table/  GET CREATE RETRIEVE

http://127.0.0.1:8000/Order/

{
  "table": 1,
  "status": "pending",
  "items": [
    { "menu_item": 3, "quantity": 2 }
  ]
}