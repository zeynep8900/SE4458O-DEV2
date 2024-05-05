# rabbitmq
# Payment Service
- Usage
* To make a payment, you need to send a POST request. Here's an example request body:
{
  "amount": 1000,
  "currency": "TRY",
  "card_number": "1234567812345678",
  "expiry_date": "12/28",
  "cvv": "123"
}
* You can use curl to send an example request:
curl http://localhost:5000/make_payment
<img width="1433" alt="image" src="https://github.com/zeynep8900/SE4458O-DEV2/assets/93615577/d3596642-687e-4bba-a1f6-fa70973cd677">
- Works
  The Flask application accepts payment requests at the /make_payment endpoint.
  The process_payment_request function sends the payment request to RabbitMQ.
  The payment_queue queue on RabbitMQ processes payment requests.
  The callback function receives the payment request and calls the process_payment function.
  The process_payment function processes the payment transaction.
  
