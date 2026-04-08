import from byllm.llm { Model }

# Initialize the LLM
glob llm = Model(model_name="gemini/gemini-2.5-flash");


# Ingredient Nodes

node Ingredient {
    has name: str;
    has available: bool = False;

    can check with MealAgent entry {
        if self.available {
            visitor.pantry += [self.name];
        }
    }
}

# Chef Node

node Chef {
    can cook with MealAgent entry {
        visitor.recipe = visitor.create_recipe(visitor.pantry);
    }
}


# Walker (Agent)

walker MealAgent {
    has pantry: list[str] = [];
    has recipe: str = "";

    can start with `root entry {
        visit [-->(`?Ingredient)];
    }

    """Create a simple recipe suggestion given available ingredients."""
    def create_recipe(pantry: list[str]) -> str by llm();
}

walker ChefWalker(MealAgent) {
    can get_recipe with `root entry {
        visit [-->(`?Chef)];
    }
}

# Example Run

with entry {
    root ++> Ingredient(name="rice", available=True);
    root ++> Ingredient(name="beans", available=True);
    root ++> Ingredient(name="chicken", available=False);
    root ++> Ingredient(name="tomatoes", available=True);
    root ++> Chef();

    agent = ChefWalker() spawn root;
    print("Available Ingredients:", agent.pantry);
    print("Suggested Recipe:");
    print(agent.recipe);
}
