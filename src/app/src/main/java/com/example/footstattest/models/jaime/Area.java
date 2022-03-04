package com.example.footstattest.models.jaime;

public class Area {
    private Integer id;
    private String name;

    // Constructor
    public Area(Integer id, String name){
        this.id = id;
        this.name = name;
    }

    //Getters and Setters

    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
