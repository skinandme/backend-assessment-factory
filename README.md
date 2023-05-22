# Skin + Me - Tech Assessment - Backend (Factory)

## The Task
We would like you to build a small Python web application (preferably using the Flask framework and SQLAlchemy) that integrates to a fictional shipping provider (think about Royal Mail or DHL), and send them customer orders to deliver on a periodic basis.

1.  Provide an interface to send customer orders to a fictional shipping provider (in the design, keep in mind in the future we could have multiple providers)
2.  Provide an interface that will allow the shipping provider to communicate events back to our system. Such events could be:
    1.  waiting for collection
    2.  in transit
    3.  delivered
    4.  failed to deliver
3.  Produce a mechanism to ship customer orders periodically based on their scheduled shipping interval
    1.  weekly
    2.  montly

### Tips
1.  Feel free to seed your database with static customer orders, we don't expect you to build an interface to create orders.
2.  We don't expect you to integrate to a real shipping provider. Just use a fictional endpoint where you could send orders to.
3.  This is obviously a broad task, we don't expect you to create something that is fully functional.
4.  By giving you a lot of freedom we want you to be able to demonstrate your skills in terms of how to structure a codebase.

## Further Guidance
So you know what we are looking for, the following is a list of themes we will use to assess your work.

- Knowledge and understanding of Python, Relational Databases and general backend development (to a lesser extent, we will also be considering your knowledge of SQLAlchemy and Flask, but this will not form the majority of the assessment).
- Data models definition
- Understanding of architecture and system design.
- Clean code and use of standards.
- Awareness of testing and testability.
- Consideration given to productionisation.
- Comments in your code for anything you want to convey your thought process or what you might do given more time.
- README on how to start your project, plus any other information you feel is relevant.
- We would like you to create a private repository in your github account and commit your code to it. We would urge you to commit relatively frequently so we can get an idea of your style and approach
