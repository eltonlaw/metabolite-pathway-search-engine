drop table if exists searches;
create table searches(
    id integer primary key autoincrement,
    cell text not null,
    cell_strain text not null,
    input_chemical text not null,
    output_chemical text not null
);
