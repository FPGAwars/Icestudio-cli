{
  "version": "1.2",
  "package": {
    "name": "",
    "version": "",
    "description": "",
    "author": "",
    "image": ""
  },
  "design": {
    "board": "alhambra-ii",
    "graph": {
      "blocks": [
        {
          "id": "96f89203-5c84-42f9-aa6b-73ba303d8790",
          "type": "basic.input",
          "data": {
            "name": "",
            "virtual": false,
            "pins": [
              {
                "index": "0",
                "name": "NULL",
                "value": "NULL"
              }
            ],
            "clock": false
          },
          "position": {
            "x": -776,
            "y": -432
          }
        },
        {
          "id": "dcde142a-e503-48d4-afbe-8c55cac29813",
          "type": "basic.output",
          "data": {
            "name": "",
            "virtual": false,
            "pins": [
              {
                "index": "0",
                "name": "NULL",
                "value": "NULL"
              }
            ]
          },
          "position": {
            "x": -520,
            "y": -432
          }
        }
      ],
      "wires": [
        {
          "source": {
            "block": "96f89203-5c84-42f9-aa6b-73ba303d8790",
            "port": "out"
          },
          "target": {
            "block": "dcde142a-e503-48d4-afbe-8c55cac29813",
            "port": "in"
          }
        }
      ]
    }
  },
  "dependencies": {}
}