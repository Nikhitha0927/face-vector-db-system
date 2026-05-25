from db import engine


class TransactionService:

    @staticmethod
    def execute_transaction(callback):

        with engine.begin() as conn:

            try:
                callback(conn)

            except Exception as e:

                print("Transaction Failed")

                raise e