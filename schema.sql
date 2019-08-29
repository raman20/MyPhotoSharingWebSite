 drop table if exists user;
		create table user(
				name text not null,
				email text not null,
				password text not null
			);