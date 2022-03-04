package com.example.footstattest.models.jaime;

public class Competition {
    private Integer id;
    private Area area;
    private String name;
    private String code;
    private String plan;
    private String lastUpdated;

    // Constructor
    public Competition(Integer id, Area area, String name, String code, String plan, String lastUpdated){
        this.id = id;
        this.area = area;
        this.name = name;
        this.code = code;
        this.plan = plan;
        this.lastUpdated = lastUpdated;
    }

    // Getters and Setters
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public Area getArea() {
        return area;
    }
    public void setArea(Area area) {
        this.area = area;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }
    public void setCode(String code) {
        this.code = code;
    }
    public String getPlan() {
        return plan;
    }
    public void setPlan(String plan) {
        this.plan = plan;
    }
    public String getLastUpdated() {
        return lastUpdated;
    }
    public void setLastUpdated(String lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
}
