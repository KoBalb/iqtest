import braintree
import os
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=braintree.Environment.Sandbox,
        merchant_id=os.getenv('merchant_id'),
        public_key=os.getenv('public_key'),
        private_key=os.getenv('private_key')
    )
)

class BraintreeConfig:
    @staticmethod
    def generate_client_token():
        return gateway.client_token.generate()

    @staticmethod
    def create_transaction(nonce, amount):
        return gateway.transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True
            }
        })

