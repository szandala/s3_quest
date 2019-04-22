from models import Base, User
import connection

engine = connection.get_engine()
if not engine.dialect.has_table(engine, "users"):

    Base.metadata.create_all(bind=connection.get_engine())

    users = [
        User(name="Ebenezer Scrooge", address="4 Milbourne St, Blackpool FY1 3ER"),
        User(name="Bruce Wayne", address="Wayne Manor, 1007 Mountain Drive, Gotham"),
        User(name="Count Dracula", address="Strada General Traian Mosoiu 24, Bran 507025"),
        User(name="Nicolas Flamel", address="51 rue de Montmorency, Paris"),
        User(name="Tony Stark", address="10880 Malibu Point, Florida"),
        User(name="Peter Parker", address="20 Ingram Street, New York"),
        User(name="Harry Potter", address="Privet Drive 4, the cupboard under the stairs")
    ]

    ss = connection.get_session()
    ss.add_all(users)
    ss.commit()

    print("DB initialization completed")

else:
    print("Nothing to do, table 'users' exists")
