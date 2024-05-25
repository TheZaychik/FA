import json
from functools import partial
from http.server import HTTPServer, BaseHTTPRequestHandler


class DatabaseConnector:
    def __init__(self) -> None:
        self._data = {}

    def __enter__(self):
        with open("./db.json", "r") as f:
            self._data = json.load(f)
        return self

    def __exit__(self, *args):
        with open("./db.json", "w") as f:
            json.dump(self._data, f)

    def _to_table(self, data):
        return [data[key] for key in data.keys()]

    def get_data_by_id(self, item_id):
        if self._data.get(item_id):
            return json.dumps(self._to_table({item_id: self._data[item_id]}))
        else:
            return None
    def get_data(self):
        return json.dumps(self._to_table(self._data))
    
    def add_item(self, new_item):
        new_id = self._data.keys().__len__()
        self._data[new_id] = {"id": new_id, "data": new_item["data"]}
        return new_id


class HTTPHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server, database) -> None:
        self.db_conn: DatabaseConnector = database
        super().__init__(request, client_address, server)

    def _set_headers(self, code, content_type="application/json"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def response_404(self, text="404 Not Found"):
        self._set_headers(404, "text/plain")
        self.wfile.write(text.encode("utf-8"))
    
    def response_400(self, text="400 Bad Request"):
        self._set_headers(400, "text/plain")
        self.wfile.write(text.encode("utf-8"))
    
    def response_200(self, data=None):
        self._set_headers(200)
        if data is not None:
            self.wfile.write(data.encode("utf-8"))
    
    def do_GET(self):
        if self.path == "/":
            self.response_200(self.db_conn.get_data())

        elif self.path.startswith("/") and any(char.isdigit() for char in self.path):
            item_id = int(self.path.split("/")[-1])
            data = self.db_conn.get_data_by_id(item_id)
            if data:
                self.response_200(data)
            else:
                self.response_404(f"Item with ID {item_id} does not exists")
        else:
            self.response_404()

    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers["Content-Length"])
            post_data_bytes = self.rfile.read(content_length).decode("utf-8")

            try:
                new_item = json.loads(post_data_bytes)
            except json.JSONDecodeError:
                self.response_400()
                return

            if "data" not in new_item.keys() or not isinstance(new_item["data"], str):  # check structure
                self.response_400()
                return

            new_id = self.db_conn.add_item(new_item)
            self.response_200(json.dumps({"id": new_id}))
        else:
            self.response_404()


with DatabaseConnector() as db_conn:
    handler = partial(HTTPHandler, database=db_conn)
    httpd = HTTPServer(("localhost", 8080), handler)
    httpd.serve_forever()
