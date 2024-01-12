# Grocery Store Application-Python

Brief description of your project.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git

   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo

   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

5. Set up the database:

   ```bash
   # Run migrations
   python manage.py migrate

   # Create a superuser (optional)
   python manage.py createsuperuser
   ```

### UI Mockups

---

### Technicle Architecture

**3 Tier Software Application**

UI (HTML/CSS/JS/Bootstrap) <--> Backend (Python Flask Server) <--> MySQL

---

### Database Commands

Create Table - products

```sql
CREATE TABLE `grocery_store`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  `uom_id` INT NOT NULL,
  `price_per_unit` DOUBLE NOT NULL,
  PRIMARY KEY (`product_id`))
```

Create Table - uom

```sql
CREATE TABLE `grocery_store`.`uom` (
  `uom_id` INT NOT NULL AUTO_INCREMENT,
  `uom_name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`uom_id`));
```

Insert Data - uom

```sql
INSERT INTO `grocery_store`.`uom` (`uom_id`, `uom_name`) VALUES ('1', 'each');
INSERT INTO `grocery_store`.`uom` (`uom_id`, `uom_name`) VALUES ('2', 'kg');
```

Insert Data - products

```sql
INSERT INTO `grocery_store`.`products` (`product_id`, `name`, `uom_id`, `price_per_unit`) VALUES ('2', 'rice', '2', '200');
```

Setup Foreign Key - products table

```sql
ALTER TABLE `grocery_store`.`products`
ADD INDEX `fk_uom_id_idx` (`uom_id` ASC) VISIBLE;
;
ALTER TABLE `grocery_store`.`products`
ADD CONSTRAINT `fk_uom_id`
  FOREIGN KEY (`uom_id`)
  REFERENCES `grocery_store`.`uom` (`uom_id`)
  ON DELETE NO ACTION
  ON UPDATE RESTRICT;
```
