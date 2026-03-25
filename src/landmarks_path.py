landmarks = [
    {
        "id": 1,
        "name": "Nhà hàng Nam Bộ",
        "latitude": 10.790002,
        "longitude": 106.729577
    },
    {
        "id": 2,
        "name": "Bamos Coffee",
        "latitude": 10.793092,
        "longitude": 106.711534
    },
    {
        "id": 3,
        "name": "HCMC University of Economics and Finance",
        "latitude": 10.797423,
        "longitude": 106.703721
    },
    {
        "id": 4,
        "name": "Pizza 4P's Saigon Pearl",
        "latitude": 10.789303,
        "longitude": 106.720775
    },
    {
        "id": 5,
        "name": "Van Thanh Park Station",
        "latitude": 10.796509,
        "longitude": 106.716143
    },
    {
        "id": 6,
        "name": "153Bis Xo Viet Nghe Tinh",
        "latitude": 10.796233,
        "longitude": 106.709853
    },
    {
        "id": 7,
        "name": "Landmark 81",
        "latitude": 10.79507,
        "longitude": 106.722156
    },
    {
        "id": 8,
        "name": "Van Thanh Tourist Village",
        "latitude": 10.798149,
        "longitude": 106.715734
    },
    {
        "id": 9,
        "name": "MOTTO RAMEN 1",
        "latitude": 10.793425,
        "longitude": 106.718463
    },
    {
        "id": 10,
        "name": "Ollin Café",
        "latitude": 10.789445,
        "longitude": 106.729892
    },
    {
        "id": 11,
        "name": "ASA Bistro",
        "latitude": 10.790863,
        "longitude": 106.722187
    },
    {
        "id": 12,
        "name": "Dong Co Goat Meat",
        "latitude": 10.786943,
        "longitude": 106.726695
    },
    {
        "id": 13,
        "name": "Chang Vang Rooftop",
        "latitude": 10.788001,
        "longitude": 106.724973
    },
    {
        "id": 14,
        "name": "HUTECH University",
        "latitude": 10.80159,
        "longitude": 106.714466
    },
    {
        "id": 15,
        "name": "Hong Bang International University",
        "latitude": 10.800315,
        "longitude": 106.706421
    },
    {
        "id": 16,
        "name": "Hanuri Korean Fast Food",
        "latitude": 10.794337,
        "longitude": 106.708685
    },
    {
        "id": 17,
        "name": "White Lotus Heritage Hotel",
        "latitude": 10.792312,
        "longitude": 106.709712
    },
    {
        "id": 18,
        "name": "Pearl Plaza",
        "latitude": 10.799835,
        "longitude": 106.718457
    },
    {
        "id": 19,
        "name": "Glory Glory Riverside",
        "latitude": 10.789299,
        "longitude": 106.725972
    },
    {
        "id": 20,
        "name": "Darlington House XVNT",
        "latitude": 10.799553,
        "longitude": 106.712047
    },
    {
        "id": 21,
        "name": "Terracotta Villa Saigon",
        "latitude": 10.798964,
        "longitude": 106.707629
    }
]


paths = [
    {
        "node_a": 1,
        "node_b": 10,
        "distance": 86/1000,
        "time": 1/60,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 13,
        "node_b": 11,
        "distance": 0.3,
        "time": 1/60,
        "risk": 0.4,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 10,
        "node_b": 12,
        "distance": 0.8,
        "time": 1/30,
        "risk": 0.4,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 12,
        "node_b": 7,
        "distance": 5.2,
        "time": 13/60,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 19,
        "distance": 0.8,
        "time": 1/20,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 9,
        "node_b": 19,
        "distance": 1,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 4,
        "node_b": 9,
        "distance": 0.85,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 15,
        "node_b": 3,
        "distance": 0.5,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 3,
        "node_b": 21,
        "distance": 1.9,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 6,
        "distance": 0.55,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.6,
        "is_directed": True # a -> b
    },
    {
        "node_a": 16,
        "node_b": 17,
        "distance": 1.7,
        "time": 7/60,
        "risk": 0.5,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 17,
        "distance": 0.35,
        "time": 1/30,
        "risk": 0.4,
        "traffic_congestion": 0.6,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 2,
        "node_b": 9,
        "distance": 1.3,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 9,
        "node_b": 5,
        "distance": 1.2,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 8,
        "distance": 0.4,
        "time": 1/30,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 8,
        "node_b": 18,
        "distance": 2,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 18,
        "node_b": 14,
        "distance": 0.5,
        "time": 1,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 9,
        "node_b": 1,
        "distance": 3.2,
        "time": 1/10,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 13,
        "node_b": 12,
        "distance": 0.35,
        "time": 1/60,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": False # a <-> b
    },
    {
        "node_a": 21,
        "node_b": 15,
        "distance": 1.2,
        "time": 1/20,
        "risk": 0.3,
        "traffic_congestion": 0.5,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 16,
        "distance": 0.23,
        "time": 1/50,
        "risk": 0.2,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 20,
        "distance": 3,
        "time": 1/6,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 9,
        "distance": 1.4,
        "time": 1/12,
        "risk": 0.2,
        "traffic_congestion": 0.3,
        "is_directed": True # a -> b
    },
    {
        "node_a": 14,
        "node_b": 20,
        "distance": 0.95,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 21,
        "distance": 2,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 4,
        "distance": 1.4,
        "time": 1/10,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 11,
        "node_b": 18,
        "distance": 4.7,
        "time": 11/60,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 3,
        "node_b": 16,
        "distance": 2,
        "time": 1/10,
        "risk": 0.7,
        "traffic_congestion": 0.9,
        "is_directed": True # a -> b
    },
    {
        "node_a": 15,
        "node_b": 14,
        "distance": 4.2,
        "time": 2/15,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 10,
        "node_b": 19,
        "distance": 4.9,
        "time": 11/60,
        "risk": 0.5,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 21,
        "distance": 1.3,
        "time": 1/15,
        "risk": 0.3,
        "traffic_congestion": 0.2,
        "is_directed": True # a -> b
    },
    {
        "node_a": 5,
        "node_b": 2,
        "distance": 2,
        "time": 1/12,
        "risk": 0.3,
        "traffic_congestion": 0.4,
        "is_directed": True # a -> b
    },
    {
        "node_a": 20,
        "node_b": 8,
        "distance": 1.4,
        "time": 2/15,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 7,
        "node_b": 18,
        "distance": 1.9,
        "time": 1/10,
        "risk": 0.4,
        "traffic_congestion": 0.7,
        "is_directed": True # a -> b
    },
    {
        "node_a": 3,
        "node_b": 6,
        "distance": 3.1,
        "time": 9/60,
        "risk": 0.6,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 6,
        "node_b": 5,
        "distance": 2.9,
        "time": 7/60,
        "risk": 0.6,
        "traffic_congestion": 0.8,
        "is_directed": True # a -> b
    },
    {
        "node_a": 2,
        "node_b": 6,
        "distance": 0.9,
        "time": 1/15,
        "risk": 0.6,
        "traffic_congestion": 0.6,
        "is_directed": True # a -> b
    },
]
