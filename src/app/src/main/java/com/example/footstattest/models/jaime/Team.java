package com.example.footstattest.models.jaime;

public class Team {
    private Integer id;
    private String name;
    private String crestUrl;

    public Team(Integer id, String name, String crestUrl){
        this.id = id;
        this.name = name;
        this.crestUrl = crestUrl;
    }

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
    public String getCrestUrl() {
        return crestUrl;
    }
    public void setCrestUrl(String crestUrl) {
        this.crestUrl = crestUrl;
    }
}
