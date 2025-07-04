gcloud compute networks vpc-access connectors create my-vpc-connector \
  --region=us-central1 \
  --network=default \
  --range=10.8.0.0/28

gcloud compute addresses create my-static-ip \
  --region=us-central1

gcloud compute routers create my-nat-router \
  --network=default \
  --region=us-central1

gcloud compute routers nats create my-nat-config \
  --router=my-nat-router \
  --region=us-central1 \
  --nat-external-ip-pool=my-static-ip \
  --nat-all-subnet-ip-ranges


Lembrar de marcar a opção de Usar VPC sem Servidor
Lembrar de marcar Encaminhar todo tráfego para a VPC
