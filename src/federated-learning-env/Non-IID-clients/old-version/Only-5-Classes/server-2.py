import tensorflow as tf
import flwr as fl

strategy = fl.server.strategy.FedAvg(min_available_clients=3,fraction_fit=0.5,fraction_eval=1.0)

fl.server.start_server(server_address='[::]:8082',config={"num_rounds": 400},strategy=strategy)


