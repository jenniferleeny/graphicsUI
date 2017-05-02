drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  jpeg_file text not null,
  bbox0_x integer,
  bbox0_y integer,
  bbox0_h integer,
  bbox0_w integer, 
  bbox1_x integer,
  bbox1_y integer,
  bbox1_h integer,
  bbox1_w integer, 
  human text not null
);
