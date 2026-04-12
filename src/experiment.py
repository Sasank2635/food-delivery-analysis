def ab_test_design():
    return {
        "control": "Normal delivery partner allocation",
        "test": "Increase delivery partners during peak hours",
        "metrics": [
            "average_delivery_time",
            "order_completion_rate"
        ]
    }